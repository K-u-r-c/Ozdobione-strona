# Generated by Django 5.1.5 on 2025-01-26 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_alter_formfield_options_alter_formfield_field_type_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formfield',
            options={'ordering': ['order'], 'verbose_name': 'Pole formularza', 'verbose_name_plural': 'Pola formularza'},
        ),
        migrations.AddField(
            model_name='formfield',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Kolejność'),
        ),
    ]
