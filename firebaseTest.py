from firebase import firebase
firebase  = firebase.FirebaseApplication("https://finger-number-detection-default-rtdb.asia-southeast1.firebasedatabase.app/",None)
# print(firebase.get("/data",None))
firebase.put("/data","finger_number",2)