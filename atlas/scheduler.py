from apscheduler.schedulers.background import BackgroundScheduler
from django.utils.timezone import now
from datetime import datetime, timedelta
from .models import FinishedProduct

def deduct_quantities():
    """
    Deducts a fixed amount from all finished products.
    Runs at a fixed time (for testing: 3 minutes from now).
    """
    amount_to_deduct = 50  # Set deduction amount

    finished_products = FinishedProduct.objects.all()
    for product in finished_products:
        if product.quantity > amount_to_deduct:
            product.quantity -= amount_to_deduct
            product.save()
        else:
            product.quantity = 0  # Prevent negative values
            product.save()

    print(f"Deduction executed at {now()} - {amount_to_deduct} units deducted.")

def start_scheduler():
    scheduler = BackgroundScheduler()

    # Calculate time 3 minutes from now
    test_time = datetime.now() + timedelta(minutes=1)

    scheduler.add_job(
        deduct_quantities,
        'cron',
        hour=test_time.hour,
        minute=test_time.minute
    )

    scheduler.start()
    print(f"Scheduler started. Task will run at {test_time.strftime('%H:%M:%S')}")

# from apscheduler.schedulers.background import BackgroundScheduler
# from django.utils.timezone import now
# from .models import FinishedProduct

# def deduct_quantities():
#     """
#     Deducts a fixed amount from all finished products at scheduled times.
#     Runs 3 times a day at fixed times.
#     """
#     amount_to_deduct = 50  # Set your deduction amount here

#     finished_products = FinishedProduct.objects.all()
#     for product in finished_products:
#         if product.quantity > amount_to_deduct:
#             product.quantity -= amount_to_deduct
#             product.save()
#         else:
#             product.quantity = 0  # Prevent negative values
#             product.save()

#     print(f"Deduction executed at {now()} - {amount_to_deduct} units deducted.")

# def start_scheduler():
#     scheduler = BackgroundScheduler()

#     # Set specific times (24-hour format)
#     fixed_times = ["08:00", "14:00", "22:00"]  # Change these times as needed

#     for time_str in fixed_times:
#         hour, minute = map(int, time_str.split(":"))
#         scheduler.add_job(deduct_quantities, 'cron', hour=hour, minute=minute)

#     scheduler.start()
#     print("Scheduler started. Tasks will run at:", fixed_times)
