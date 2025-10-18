from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    class DiscountType(models.TextChoices):
        NONE = "NONE", "ไม่มีส่วนลด"
        PERCENT = "PERCENT", "ลดตามเปอร์เซ็นต์"
        FIXED = "FIXED", "ลดตามจำนวนเงิน"

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    image = models.FileField(upload_to="product_images/", null=True, blank=True)
    discount_type = models.CharField(max_length=8, choices=DiscountType.choices, default=DiscountType.NONE)
    discount_value = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)
    is_active = models.BooleanField(default=True)

    def discount_percent(self):
        if self.discount_type == "PERCENT":
            return self.discount_value
        elif self.discount_type == "FIXED":
            return (self.discount_value / self.price) * 100
        return 0

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=True, blank=True)
    image = models.FileField(upload_to="customer_images/", blank=True, null=True)
    wishlist = models.ManyToManyField(Product)

class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    address = models.TextField()
    district = models.CharField(max_length=50)
    sub_district = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.full_name} ({self.phone}) - {self.address}, {self.sub_district}, {self.district}, {self.province}, {self.postal_code}"

class CartItem(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class DiscountCode(models.Model):
    class CodeType(models.TextChoices):
        PERCENT = "PERCENT", "ลดตามเปอร์เซ็นต์"
        FIXED = "FIXED", "ลดตามจำนวนเงิน"
    code = models.CharField(max_length=50, unique=True)
    code_type = models.CharField(max_length=8, choices=CodeType.choices)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    min_order_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    max_discount_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    usage_count = models.PositiveIntegerField(default=0)

class Order(models.Model):
    class OrderStatus(models.TextChoices):
        PENDING = "PENDING", "รอดำเนินการ"
        SHIPPING = "SHIPPING", "กำลังจัดส่ง"
        DELIVERED = "DELIVERED", "จัดส่งสำเร็จ"
        CANCELLED = "CANCELLED", "ยกเลิกคำสั่งซื้อ"
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    discount_code = models.ForeignKey(DiscountCode, on_delete=models.PROTECT, null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    shipping_address = models.TextField()
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=OrderStatus.choices)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class Payment(models.Model):
    class PaymentStatus(models.TextChoices):
        PENDING = "PENDING", "รอการตรวจสอบ"
        VERIFIED = "VERIFIED", "ได้รับการยืนยัน"
        REJECTED = "REJECTED", "ปฏิเสธ"
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    payment_date = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    slip_image = models.FileField(upload_to="slip_images/")
    status = models.CharField(max_length=10, choices=PaymentStatus.choices)
    