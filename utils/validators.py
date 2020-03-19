from marshmallow import validate, Schema, fields


class Authors(Schema):
    """Nested Schema"""
    first_name = fields.String(required=False, validate=validate.Length(min=1))
    last_name = fields.String(required=False, validate=validate.Length(min=1))
    email = fields.Email(
        required=False,
        validate=validate.Regexp("^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$")
    )
    faculty = fields.String(required=False, validate=validate.Length(min=1))


class Actors(Schema):
    """Nested Schema"""
    first_name = fields.String(required=False, validate=validate.Length(min=1))
    last_name = fields.String(required=False, validate=validate.Length(min=1))
    role = fields.String(required=False, validate=validate.Length(min=1))


class General(Schema):
    """ Nested Schema"""
    authors = fields.List(fields.Nested(Authors), required=False, validate=validate.Length(1))
    actors = fields.List(fields.Nested(Actors), required=False, validate=validate.Length(1))
    description = fields.String(required=False, validate=validate.Length(min=1))
    title = fields.String(required=False, validate=validate.Length(min=1))



class GetDocumentsValidator(Schema):
    """ Request body schema for the endpoint /api/documents"""
    general = fields.List(fields.Nested(General, required=False), required=False)

    publication_date = fields.List(
        fields.Date(),
        required=False,
        allow_none=False,
        validate=validate.Length(min=1)
    )

    tags = fields.List(
        fields.String(),
        required=False,
        validate=validate.Length(min=1)
    )

    incident_dates = fields.List(
        fields.Date(),
        required=False,
        validate=validate.Length(min=1))

    infrastructure_type = fields.List(
        fields.String(),
        required=False,
        validate=validate.Length(min=1))

    damage_type = fields.List(
        fields.String(),
        required=False,
        validate=validate.Length(min=1))

    language = fields.String(
        required=False,
        default='English',
        validate=validate.Length(min=1)
    )


class GetDocIdValidator(Schema):
    """ Request body schema for the endpoint /api/documents/view/<doc_id>/"""
    doc_id = fields.String(required=True, validate=validate.Length(min=1))


class GetCollaboratorRequestValidator(Schema):
    """ Request body schema for the endpoint /api/collabrequest/"""
    first_name = fields.String(required=True, validate=validate.Length(min=1))
    last_name = fields.String(required=True, validate=validate.Length(min=1))
    email = fields.Email(
        required=True,
        validate=validate.Regexp("^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$")
    )
    faculty = fields.String(required=True, validate=validate.Length(min=1))


class GetComparisonValidator(Schema):
    """ Request body schema for the endpoint /api/documents/view/<doc_id>/"""
    xcat = fields.String(required=True, validate=validate.Length(min=1))
    ycat = fields.String(required=True, validate=validate.Length(min=1))
    xvalue = fields.String(required=True, validate=validate.Length(min=1))
    yvalue = fields.String(required=True, validate=validate.Length(min=1))