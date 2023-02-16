from app_name.extensions import db


class ExampleModel_one(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f'<ExampleModel_one "{self.id}">'


class ExampleModel_two(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f'<ExampleModel_two "{self.id}">'
