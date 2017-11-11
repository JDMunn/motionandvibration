from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute


class SubmissionModel(Model):

    class Meta:
        table_name = "motionandvibration"

    email = UnicodeAttribute()
    name = UnicodeAttribute()
    category = UnicodeAttribute()
    focus = UnicodeAttribute()
    title = UnicodeAttribute()
    description = UnicodeAttribute()
    link = UnicodeAttribute()
    submission_id = UnicodeAttribute(hash_key=True)
