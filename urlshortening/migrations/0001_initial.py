from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('short_id', models.SlugField(primary_key=True, serialize=False)),
                ('url', models.URLField()),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('is_expired', models.BooleanField(default=False)),
                ('redirect_count', models.IntegerField(default=0)),
            ],
        ),
    ]
