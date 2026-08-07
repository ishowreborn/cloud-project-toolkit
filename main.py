# import boto3
# from botocore.exceptions import ClientError


# # Connect to EC2
# ec2 = boto3.client("ec2")


# # --------------------------------------------------
# # LIST EC2 INSTANCES
# # --------------------------------------------------

# def list_instances():

#     try:
#         response = ec2.describe_instances()

#         print("\n========== EC2 INSTANCES ==========\n")

#         found_instance = False

#         for reservation in response["Reservations"]:

#             for instance in reservation["Instances"]:

#                 found_instance = True

#                 # Get instance name
#                 name = "No Name"

#                 if "Tags" in instance:

#                     for tag in instance["Tags"]:

#                         if tag["Key"] == "Name":
#                             name = tag["Value"]

#                 print("=" * 40)
#                 print("Name       :", name)
#                 print("Instance ID:", instance["InstanceId"])
#                 print("State      :", instance["State"]["Name"])

#                 if "PublicIpAddress" in instance:
#                     print("Public IP  :", instance["PublicIpAddress"])
#                 else:
#                     print("Public IP  : None")

#                 print("=" * 40)

#         if not found_instance:
#             print("No EC2 instances found.")

#     except ClientError as error:

#         print("\nAWS Error:", error)


# # --------------------------------------------------
# # START EC2 INSTANCE
# # --------------------------------------------------

# def start_instance():

#     instance_id = input("\nEnter Instance ID to start: ").strip()

#     if not instance_id:
#         print("Instance ID cannot be empty.")
#         return

#     confirm = input(
#         f"Are you sure you want to START {instance_id}? (yes/no): "
#     ).lower()

#     if confirm != "yes":
#         print("Operation cancelled.")
#         return

#     try:

#         response = ec2.start_instances(
#             InstanceIds=[instance_id]
#         )

#         print("\nEC2 instance start command sent successfully.")
#         print("Instance ID:", instance_id)

#     except ClientError as error:

#         print("\nAWS Error:", error)


# # --------------------------------------------------
# # STOP EC2 INSTANCE
# # --------------------------------------------------

# def stop_instance():

#     instance_id = input("\nEnter Instance ID to stop: ").strip()

#     if not instance_id:
#         print("Instance ID cannot be empty.")
#         return

#     confirm = input(
#         f"Are you sure you want to STOP {instance_id}? (yes/no): "
#     ).lower()

#     if confirm != "yes":
#         print("Operation cancelled.")
#         return

#     try:

#         response = ec2.stop_instances(
#             InstanceIds=[instance_id]
#         )

#         print("\nEC2 instance stop command sent successfully.")
#         print("Instance ID:", instance_id)

#     except ClientError as error:

#         print("\nAWS Error:", error)


# # --------------------------------------------------
# # REBOOT EC2 INSTANCE
# # --------------------------------------------------

# def reboot_instance():

#     instance_id = input("\nEnter Instance ID to reboot: ").strip()

#     if not instance_id:
#         print("Instance ID cannot be empty.")
#         return

#     confirm = input(
#         f"Are you sure you want to REBOOT {instance_id}? (yes/no): "
#     ).lower()

#     if confirm != "yes":
#         print("Operation cancelled.")
#         return

#     try:

#         response = ec2.reboot_instances(
#             InstanceIds=[instance_id]
#         )

#         print("\nEC2 instance reboot command sent successfully.")
#         print("Instance ID:", instance_id)

#     except ClientError as error:

#         print("\nAWS Error:", error)


# # --------------------------------------------------
# # EC2 HEALTH CHECK
# # --------------------------------------------------

# def health_check():

#     instance_id = input("\nEnter Instance ID for health check: ").strip()

#     if not instance_id:
#         print("Instance ID cannot be empty.")
#         return

#     try:

#         response = ec2.describe_instance_status(
#             InstanceIds=[instance_id],
#             IncludeAllInstances=True
#         )

#         if not response["InstanceStatuses"]:

#             print("\nInstance not found or status information unavailable.")
#             return

#         status = response["InstanceStatuses"][0]

#         print("\n========== EC2 HEALTH CHECK ==========")

#         print("Instance ID    :", status["InstanceId"])
#         print(
#             "Instance State :",
#             status["InstanceState"]["Name"]
#         )
#         print(
#             "System Status  :",
#             status["SystemStatus"]["Status"]
#         )
#         print(
#             "Instance Status:",
#             status["InstanceStatus"]["Status"]
#         )

#         if (
#             status["SystemStatus"]["Status"] == "ok"
#             and status["InstanceStatus"]["Status"] == "ok"
#         ):

#             print("\nHealth Check: HEALTHY")

#         else:

#             print("\nHealth Check: NOT HEALTHY")

#         print("=" * 40)

#     except ClientError as error:

#         print("\nAWS Error:", error)


# # --------------------------------------------------
# # MAIN MENU
# # --------------------------------------------------

# while True:

#     print("\n")
#     print("========================================")
#     print("          CLOUD PROJECT TOOLKIT")
#     print("========================================")
#     print("1. List EC2 Instances")
#     print("2. Start EC2 Instance")
#     print("3. Stop EC2 Instance")
#     print("4. Reboot EC2 Instance")
#     print("5. EC2 Health Check")
#     print("6. Exit")
#     print("========================================")

#     choice = input("Enter your choice: ").strip()

#     if choice == "1":

#         list_instances()

#     elif choice == "2":

#         start_instance()

#     elif choice == "3":

#         stop_instance()

#     elif choice == "4":

#         reboot_instance()

#     elif choice == "5":

#         health_check()

#     elif choice == "6":

#         print("\nGoodbye!")
#         break

#     else:

#         print("\nInvalid choice. Please try again.")