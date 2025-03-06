from django import forms

class IngredientSearchForm(forms.Form):
    ingredient = forms.CharField(
        label="Ingredient Name",
        max_length=100,
        required=False
    )

    # chart_type = forms.ChoiceField(
    #     label="Chart Type",
    #     choices=[
    #         ("#1", "Pie Chart"),
    #         ("#2", "Bar Chart"),
    #         ("#3", "Line Chart"),
    #     ],
    #     required=False
    # )