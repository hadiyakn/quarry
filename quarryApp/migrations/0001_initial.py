# Generated by Django 4.2.3 on 2023-08-06 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('ct_id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=80)),
            ],
            options={
                'db_table': 'tb_Category',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('fd_id', models.AutoField(primary_key=True, serialize=False)),
                ('log_id', models.IntegerField()),
                ('rec_id', models.IntegerField()),
                ('feedback', models.TextField()),
                ('reply', models.TextField()),
                ('feedback_date', models.DateField()),
            ],
            options={
                'db_table': 'tb_Feedback',
            },
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('log_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('password', models.TextField()),
                ('role', models.CharField(max_length=20)),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'tb_Login',
            },
        ),
        migrations.CreateModel(
            name='Product_type',
            fields=[
                ('tp_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_type', models.CharField(max_length=80)),
                ('stock', models.IntegerField()),
                ('image', models.CharField(max_length=50)),
                ('ct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quarryApp.category')),
            ],
            options={
                'db_table': 'tb_Product_type',
            },
        ),
        migrations.CreateModel(
            name='Vehicle_pass',
            fields=[
                ('ps_id', models.AutoField(primary_key=True, serialize=False)),
                ('v_id', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.CharField(max_length=30)),
                ('destination', models.CharField(max_length=150)),
                ('status', models.IntegerField()),
                ('log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quarryApp.login')),
            ],
            options={
                'db_table': 'tb_Vehicle_pass',
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('v_id', models.AutoField(primary_key=True, serialize=False)),
                ('owner_name', models.CharField(max_length=20)),
                ('contact_no', models.BigIntegerField()),
                ('address', models.CharField(max_length=150)),
                ('vehicle_number', models.CharField(max_length=15)),
                ('permit', models.CharField(max_length=50)),
                ('log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quarryApp.login')),
            ],
            options={
                'db_table': 'tb_Vehicle',
            },
        ),
        migrations.CreateModel(
            name='Type_spec',
            fields=[
                ('ts_id', models.AutoField(primary_key=True, serialize=False)),
                ('size', models.IntegerField()),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('tp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quarryApp.product_type')),
            ],
            options={
                'db_table': 'tb_Type_spec',
            },
        ),
        migrations.CreateModel(
            name='Order_product',
            fields=[
                ('or_id', models.AutoField(primary_key=True, serialize=False)),
                ('tp_id', models.IntegerField()),
                ('date', models.DateField()),
                ('re_date', models.DateField()),
                ('size', models.IntegerField()),
                ('load', models.IntegerField()),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('o_type', models.CharField(max_length=20)),
                ('status', models.IntegerField()),
                ('log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quarryApp.login')),
            ],
            options={
                'db_table': 'tb_Order_product',
            },
        ),
        migrations.CreateModel(
            name='Employee_register',
            fields=[
                ('emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('image', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=150)),
                ('designation', models.CharField(blank=True, max_length=50, null=True)),
                ('contact_no', models.BigIntegerField()),
                ('email', models.CharField(max_length=50)),
                ('log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quarryApp.login')),
            ],
            options={
                'db_table': 'tb_Employee_register',
            },
        ),
        migrations.CreateModel(
            name='Contractor_register',
            fields=[
                ('con_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('company', models.CharField(max_length=50)),
                ('owner_name', models.CharField(max_length=30)),
                ('licence', models.CharField(max_length=40)),
                ('company_address', models.CharField(max_length=150)),
                ('contact_no', models.BigIntegerField()),
                ('email', models.CharField(max_length=50)),
                ('log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quarryApp.login')),
            ],
            options={
                'db_table': 'tb_Contractor_register',
            },
        ),
    ]
