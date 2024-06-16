from rest_framework import serializers
from .models import Product, Stock, StockProduct

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True, read_only=True)

    class Meta:
        model = Stock
        fields = '__all__'

    def create(self, validated_data):
        positions_data = validated_data.pop('positions')
        stock = Stock.objects.create(**validated_data)
        for position_data in positions_data:
            StockProduct.objects.create(stock=stock, **position_data)
        return stock

    def update(self, instance, validated_data):
        positions_data = validated_data.pop('positions')
        positions = StockProduct.objects.filter(stock=instance)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        for position_data in positions_data:
            position = positions.filter(product=position_data.get('product')).first()
            if position:
                position.quantity = position_data.get('quantity', position.quantity)
                position.price = position_data.get('price', position.price)
                position.save()
        return instance
