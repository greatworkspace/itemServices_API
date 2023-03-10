# Generated by Django 3.2.6 on 2023-02-01 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itemCategories', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='brand_name',
        ),
        migrations.RemoveField(
            model_name='products',
            name='category',
        ),
        migrations.RemoveField(
            model_name='products',
            name='group',
        ),
        migrations.RemoveField(
            model_name='products',
            name='item',
        ),
        migrations.RemoveField(
            model_name='products',
            name='sub_group',
        ),
        migrations.AddField(
            model_name='products',
            name='description',
            field=models.TextField(default=True, verbose_name='Product Description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='frac',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='products',
            name='item_barcode',
            field=models.PositiveIntegerField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='item_name',
            field=models.CharField(default=True, max_length=120, verbose_name='Item Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='product_category',
            field=models.CharField(choices=[('Drinks', 'Drinks'), ('Pharma_Prod', 'Pharmaceuticals Product'), ('C_A', 'Children Accessories'), ('HB_Prod', 'Health and Beauty Products'), ('MW_Acc', 'Men and Women Accessories'), ('STATS', 'Stationery'), ('D_Prod', 'Dairy Product'), ('S_S', 'Sweets and Snacks')], default=True, max_length=50, verbose_name='Product Category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='purchasing_price',
            field=models.DecimalField(decimal_places=2, default=True, max_digits=9, verbose_name='Price in Naira'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='purchasing_unit',
            field=models.PositiveIntegerField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='sales_price',
            field=models.DecimalField(decimal_places=2, default=True, max_digits=9, verbose_name='Price in Naira'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='sales_unit',
            field=models.PositiveIntegerField(default=True, verbose_name='sales unit'),
            preserve_default=False,
        ),
    ]
