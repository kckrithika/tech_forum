# Generated by Django 2.0.7 on 2018-08-02 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_comment', models.TextField()),
                ('_time', models.DateTimeField(auto_now_add=True)),
                ('_answer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.Answer')),
                ('_author', models.ForeignKey(on_delete=None, to='forum.User')),
                ('_question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.Question')),
            ],
            options={
                'db_table': 'Comments',
            },
        ),
    ]
