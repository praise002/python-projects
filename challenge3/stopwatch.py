import time

# while True:
#     try:
#         input("Press Enter to continue, CTRL-C to exit")
#         start_time = time.time()  #to get current time
#         print("Timer has started")
#         while True:
#             print("Time elapsed:", round(time.time() - start_time), "secs")  #current time - start time
#             time.sleep(1)
#     except KeyboardInterrupt:
#         print("Timer has stopped")
#         end_time = time.time()
#         print("The time elapsed is", round(end_time - start_time), "secs")
#         break


"""PART2"""
run = input("Start> ")
seconds = 0
if run.lower() == "yes":
    while seconds != 10:
        print(">", seconds)
        time.sleep(1)
        seconds += 1
    print(">", seconds)