# Generated by Django 4.1.5 on 2023-01-06 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ordered_parts',
            fields=[
                ('op_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Parts',
            fields=[
                ('part_no', models.IntegerField(primary_key=True, serialize=False)),
                ('P_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Workshop_orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('W_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Workshoporders', to='User.workshop')),
                ('op_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SCP.ordered_parts')),
            ],
        ),
        migrations.CreateModel(
            name='Workshop_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_field', models.ImageField(default='no-image.jpg', height_field='imageheight', upload_to='static/images/profile/20230106-231606', width_field='imagewidth')),
                ('imagewidth', models.PositiveIntegerField(default=50, editable=False)),
                ('imageheight', models.PositiveIntegerField(default=50, editable=False)),
                ('W_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='WorkshopImg', to='User.workshop')),
            ],
        ),
        migrations.CreateModel(
            name='Store_parts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('P_name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=200)),
                ('car_make', models.CharField(max_length=50)),
                ('S_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='StoreParts', to='User.store')),
                ('part_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SCP.parts')),
            ],
        ),
        migrations.CreateModel(
            name='Store_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_field', models.ImageField(default='no-image.jpg', height_field='imageheight', upload_to='static/images/profile/20230106-231606', width_field='imagewidth')),
                ('imagewidth', models.PositiveIntegerField(default=50, editable=False)),
                ('imageheight', models.PositiveIntegerField(default=50, editable=False)),
                ('S_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='StoreInformation', to='User.store')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('price', models.FloatField(null=True)),
                ('W_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='WorkshopServices', to='User.workshop')),
            ],
        ),
        migrations.CreateModel(
            name='Part_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_field', models.ImageField(default='no-image.jpg', height_field='imageheight', upload_to='static/images/profile/20230106-231606', width_field='imagewidth')),
                ('imagewidth', models.PositiveIntegerField(default=65, editable=False)),
                ('imageheight', models.PositiveIntegerField(default=65, editable=False)),
                ('P_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SCP.parts')),
            ],
        ),
        migrations.AddField(
            model_name='ordered_parts',
            name='sp_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='StoreParts', to='SCP.store_parts'),
        ),
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_desc', models.CharField(max_length=200)),
                ('offer_price', models.IntegerField()),
                ('W_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='WorkshopOffers', to='User.workshop')),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SCP.services')),
            ],
        ),
        migrations.CreateModel(
            name='Customer_orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('C_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CustomerOders', to='User.customer')),
                ('S_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='StoreOders', to='User.store')),
                ('op_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SCP.ordered_parts')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
                ('C_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CustomerAppointment', to='User.customer')),
                ('S_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='AppointmentType', to='SCP.services')),
                ('W_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='WorkshopAppointment', to='User.workshop')),
            ],
        ),
    ]
