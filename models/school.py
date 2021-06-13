from odoo import fields, models


class SchoolProfile(models.Model):
    _name = "school.profile"

    def get_establish_date(self):
        return fields.Date.today()

    name = fields.Char(string="School Name", help="This is School Name", required=True, index=True,
                       default="This is school Name")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    is_virtual_class = fields.Boolean(string="Virtual Class Support", default=True)
    school_rank = fields.Integer(string="Rank")
    result = fields.Float(string="Result", default=1.1, digits=(2, 3))
    address = fields.Text(string="Address")

    establish_date = fields.Date(string="Establish Date", default=lambda lm: lm.get_establish_date())
    open_date = fields.Datetime(string="Open Date", default=fields.Datetime.now())

    school_type = fields.Selection([('public', 'Public School'),
                                    ('private', 'Private School')], string="Type of School",
                                   help="Please select type of school",
                                   default='private')

    documents = fields.Binary(string="Documents")
    document_name = fields.Char(string="File Name")
