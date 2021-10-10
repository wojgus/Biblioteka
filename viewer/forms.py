from django.db.models import TextField
from django.forms import (
    ModelForm, CharField, IntegerField, DateField, ModelChoiceField,
)
from viewer.models import Book, Genre


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
    tytul = CharField()
    rating = IntegerField(min_value=1, max_value=10)
    rok_wydania = DateField()
    ocena = IntegerField()
    opis = TextField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'



