# Generated by Django 4.0.3 on 2022-03-11 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_color_variant_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='created_at',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='updated_at',
            new_name='updated',
        ),
        migrations.RenameField(
            model_name='colorvariant',
            old_name='created_at',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='colorvariant',
            old_name='updated_at',
            new_name='updated',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='created_at',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='updated_at',
            new_name='updated',
        ),
        migrations.RenameField(
            model_name='productimage',
            old_name='created_at',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='productimage',
            old_name='updated_at',
            new_name='updated',
        ),
        migrations.RenameField(
            model_name='sizevariant',
            old_name='created_at',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='sizevariant',
            old_name='updated_at',
            new_name='updated',
        ),
    ]
