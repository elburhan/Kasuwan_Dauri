# Generated by Django 5.0.7 on 2024-07-14 13:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ProductServices', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='added_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_by_user_id_category', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='categories',
            name='domain_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='domain_user_id_category', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='categories',
            name='parent_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ProductServices.categories'),
        ),
        migrations.AddField(
            model_name='productquestions',
            name='answer_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answer_by_user_id_questions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productquestions',
            name='domain_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='domain_user_id_questions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productquestions',
            name='question_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions_by_user_id_questions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productreviews',
            name='domain_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='domain_user_id_reviews', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productreviews',
            name='review_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_by_user_id_reviews', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='products',
            name='added_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_by_user_id_products', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='products',
            name='category_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_id_products', to='ProductServices.categories'),
        ),
        migrations.AddField(
            model_name='products',
            name='domain_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='domain_user_id_products', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productreviews',
            name='product_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_id_reviews', to='ProductServices.products'),
        ),
        migrations.AddField(
            model_name='productquestions',
            name='product_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_id_questions', to='ProductServices.products'),
        ),
    ]
