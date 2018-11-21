# Generated by Django 2.0.7 on 2018-08-02 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_question', models.TextField()),
                ('_time', models.DateTimeField(auto_now_add=True)),
                ('_closed', models.BooleanField(default=False)),
                ('_answerer', models.ForeignKey(default=None, on_delete=None, to='forum.User')),
                ('_asker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.User')),
            ],
            options={
                'db_table': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_topic', models.CharField(max_length=50)),
                ('_parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Topic')),
            ],
            options={
                'db_table': 'Topics',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='_topic',
            field=models.ForeignKey(on_delete=None, to='forum.Topic'),
        ),
    ]