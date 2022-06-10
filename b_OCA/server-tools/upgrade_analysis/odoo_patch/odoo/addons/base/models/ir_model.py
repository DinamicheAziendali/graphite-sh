from odoo.addons.base.models import ir_model

from ...... import upgrade_log
from .....odoo_patch import OdooPatch


class IrModelConstraintPatch(OdooPatch):
    target = ir_model.IrModelConstraint
    method_names = ["_reflect_model"]

    def _reflect_model(self, model):
        """Reflect the _sql_constraints of the given model."""

        def cons_text(txt):
            return txt.lower().replace(", ", ",").replace(" (", "(")

        # map each constraint on the name of the module where it is defined
        constraint_module = {
            constraint[0]: cls._module
            for cls in reversed(type(model).mro())
            if not getattr(cls, "pool", None)
            for constraint in getattr(cls, "_local_sql_constraints", ())
        }

        data_list = []
        for (key, definition, message) in model._sql_constraints:
            conname = "%s_%s" % (model._table, key)
            module = constraint_module.get(key)
            record = self._reflect_constraint(
                model, conname, "u", cons_text(definition), module, message
            )
            if record:
                xml_id = "%s.constraint_%s" % (module, conname)
                data_list.append(dict(xml_id=xml_id, record=record))

        self.env["ir.model.data"]._update_xmlids(data_list)
        for data in data_list:
            xml_id = data.get("xml_id")
            module = xml_id.split(".")[0]
            upgrade_log.log_xml_id(self.env.cr, module, xml_id)
