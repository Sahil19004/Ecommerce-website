# Generated by Django 4.2.4 on 2023-10-08 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0009_alter_category_id_alter_order_id_alter_product_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='prod_deal',
            field=models.CharField(choices=[('HOT DEALS', 'HOT DEALS'), ('New Arraivels', 'New Arraivels')], default=0, max_length=100),
            preserve_default=False,
        ),
    ]