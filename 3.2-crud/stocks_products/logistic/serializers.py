from rest_framework import serializers

from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    # настройте сериализатор для позиции продукта на складе
    # product = serializers.SlugRelatedField(slug_field='title', queryset=Product.objects.all())
    # product = ProductSerializer()

    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), required=False, allow_null=True)
    class Meta:
        model = StockProduct
        fields = ['id', 'quantity', 'price', 'product']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        # при этом удаляя их из словаря
        positions = validated_data.pop('positions')

        stock = super().create(validated_data)
        for position in positions:
            _product = position.pop('product')
            product = Product.objects.get(id=_product.id)
            StockProduct.objects.create(
                stock=stock,
                product=product,
                **position
            )
        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)

        # здесь вам надо обновить связанные таблицы
        for position in positions:
            _product = position.pop('product')
            product = Product.objects.get(id=_product.id)
            StockProduct.objects.filter(stock=stock, product=product).update(**position)

        return stock
