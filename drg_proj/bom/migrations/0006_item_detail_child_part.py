# Generated by Django 3.0.5 on 2020-05-19 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bom', '0005_auto_20200520_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='item_detail',
            name='Child_part',
            field=models.CharField(max_length=256, null=True),
        ),
    ]