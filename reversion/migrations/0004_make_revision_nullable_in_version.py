# Generated by Django 3.2.6 on 2021-08-16 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reversion', '0003_add_m2m_relation_to_existing_versions'),
    ]
    operations = [
        migrations.AlterField(
            model_name='version',
            name='revision',
            field=models.ForeignKey(help_text='The revision that contains this version.', on_delete=django.db.models.deletion.SET_NULL,
                       null=True, to='reversion.Revision')

        )
    ]
