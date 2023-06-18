from django import forms

from places.models import TYPE_CHOICES

CAPACITY_CHOICES = (
    ("1", "Маленькая"),
    ("2", "Средняя"),
    ("3", "Большая")
)

ATTENDANCE_CHOICES = (
    ("1", "Низкая"),
    ("2", "Средняя"),
    ("3", "Высокая")
)


class MinimumEntryField(forms.MultiValueField):
    def __init__(self, *args, **kwargs):
        fields = (
            forms.IntegerField(),
            forms.CharField(),
        )
        super().__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            return (int(data_list[0]), data_list[1])
        return None


class PlaceForm(forms.Form):
    ymaps_soup = forms.CharField(label="'Ymaps page source",
                                 widget=forms.TextInput(
                                 attrs={'placeholder': 'Ymaps page source', 'size': '100'}), required=True)
    take_ymaps_name = forms.BooleanField(label='Брать название с Yandex Maps?', required=False)
    name = forms.CharField(label="Название", max_length=300, required=False)
    type = forms.ChoiceField(label='Тип', choices=TYPE_CHOICES)

    minimum_entry = forms.CharField(label="Минимальный порог входа (ПРИМЕР: 90 - чай)", max_length=300)
    socket_availability = forms.BooleanField(label='Наличие розеток', required=False)
    entertainments = forms.CharField(label="Развлечения (ПРИМЕР: телевизор, телки...)", max_length=300, required=False)
    furniture = forms.CharField(label="Мебель (ПРИМЕР: стул, стол...)", max_length=300, required=False)
    own_food_ability = forms.BooleanField(label='Возможность своей еды', required=False)
    food_availability = forms.BooleanField(label='Наличие еды', required=False)
    water_availability = forms.BooleanField(label='Наличие бесплатной воды', required=False)
    toilets_availability = forms.BooleanField(label='Наличие туалетов', required=False)
    device_rental = forms.CharField(label="Аренда техники (ПРИМЕР: ноутбук, принтер...)", max_length=300,
                                    required=False)
    consumables_rental = forms.CharField(label="Аренда расходных материалов (ПРИМЕР: картон, линейки...)",
                                         max_length=300, required=False)
    lecture_hall_rental = forms.BooleanField(label='Аренда лектория', required=False)
    capacity = forms.ChoiceField(label="Вместительность", choices=CAPACITY_CHOICES)
    crowded = forms.ChoiceField(label="Посещаемость", choices=ATTENDANCE_CHOICES)
    quiet_place_availability = forms.BooleanField(label='Наличие тихих мест', required=False)
    call_place_availability = forms.BooleanField(label='Наличие мест для созвона', required=False)

    def clean(self):
        cleaned_data = super().clean()
        take_ymaps_name = cleaned_data.get('take_ymaps_name')
        name = cleaned_data.get('name')

        if bool(take_ymaps_name) == bool(name):
            raise forms.ValidationError(
                "Должно быть заполнено название, либо выбрана функция взятия названия с Yandex Maps")

        return cleaned_data
