# Generated by Django 2.0.7 on 2018-08-02 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20180802_0808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='_answerer',
            field=models.ForeignKey(default=None, null=True, on_delete=None, to='forum.User'),
        ),
    ]