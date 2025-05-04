 # מסד נתונים לניהול חיל הים🚢

אלון ואן גלדר 216258483 ובעז זינגר 215444647

## תוכן עניינים

- [שלב 1: עיצוב ויצירת מסד נתונים](#שלב-1-עיצוב-ויצירת-מסד-נתונים)  
  - [הקדמה](#הקדמה)
  - [דיאגמרת ERD](#erd-entity-relationship-diagram)
  - [דיאגרמת DSD](#dsd-data-structure-diagram)  
  - [סקריפטים בSQL](#סקריפטים)
  - [הכנסת מידע לטבלאות](#הכנסת-מידע-לטבלאות)
  - [גיבוי](#גיבוי)  
- [שלב 2: שאילתות](#שלב-2-שאילתות)
  - [שאילתות selcect](#בחירה_מטבלאות)
  - [שאילתות delete](#בחירה_מטבלאות)
  - [שאילתות update](#בחירה_מטבלאות)







## שלב 1: עיצוב ויצירת מסד נתונים

### הקדמה
מסד הנתונים נועד לנהל ביעילות מידע על כלי שיט, צוותים, חיילים ובסיסים. המערכת מאפשרת מעקב אחר כלי שיט שונים, שיוכם לבסיסים, הצוותים המוצבים בהם, נתוני בדיקות, ופרטים אישיים של החיילים והצוותים.

#### מטרת המבנה נתונים

-ניהול כלי שיט הכוללים משחתות, צוללות, ספינות טילים וספינות מלחמה.

-שיוך כלי שיט לבסיסים ימיים ולצוותים מתאימים.

-מעקב אחר בדיקות תקופתיות של כלי השיט ונתונים תפעוליים חשובים.

-ניהול כוח האדם, הכולל צוותים, חיילים ודירוגים צבאיים.

ניהול פרטי צוותי הספינות והחיילים המשרתים בחיל הים.

#### מקרי שימוש עקריים
-מפקדי חיל הים יכולים לנהל כלי שיט ולשבץ צוותים בהתאם לכשירותם ולצרכים המבצעיים.

-מנהלי בסיסים יכולים לפקח על כלי שיט השייכים לבסיס ולנהל את הצוותים המקומיים.

-חיילים ואנשי צוות יכולים להתעדכן בפרטי כלי השיט שלהם, בבדיקות שנעשו, ובנתוני הצוותים השייכים לכל ספינה.

#### יתרונות המערכת
✔ ניהול קל של כלי שיט עם היררכיית סוגים.

✔ מעקב אחרי צוותים ובסיסים רלוונטיים.

✔ אחסון נתוני חיילים ודרגותיהם.

✔ גישה נוחה למידע תפעולי של חיל הים.

###  ERD (Entity-Relationship Diagram)    

![ERD Diagram](Stage1/ERDAndDSDFiles/ERD.png)  


###  DSD (Data Structure Diagram)   
![DSD Diagram](Stage1/ERDAndDSDFiles/DSD.jpg)  

###  סקריפטים:

- **סקריפט יצירת טבלאות:** 

✍🏻 **[`createTables.sql`](Stage1/scripts/createTables.sql)**  

- **סקריפט הכנסה לטבלאות:**

✍🏻 **[`insertTables.sql`](Stage1/scripts/insertTables.sql)**  
 
- **סקריפט מחיקת טבלאות:** 

✍🏻 **[`dropTables.sql`](Stage1/scripts/dropTables.sql)**  

- **סקריפט בחירת כל המידע מהטבלאות:**  

✍🏻 **[`selectAll.sql`](Stage1/scripts/selectAll.sql)**  


###  הכנסת מידע לטבלאות:

####  כלי ראשון: שימוש באתר [mockaro](https://www.mockaroo.com/) על מנת ליצור קובץ CSV, תקיית כל הקבצים:  **[`mockarooFiles`](Stage1/mockarooFiles)**  
דוגמא ליצירת הקבצים עבור Submarine:

![image](https://github.com/user-attachments/assets/19cd2a58-a6a9-43b7-a0a6-00f0dfc4728e)

![image](https://github.com/user-attachments/assets/340ec029-8704-4e78-b625-9b51ae449c85)

ככה נעשה עבור כל הטבלאות


####  כלי שני: יצירת סקריפט בפייתון ✍🏻 **[`insert.py`](Stage1/Programing/insert.py)**  

![image](https://github.com/user-attachments/assets/d2d95a7f-1783-45e1-88da-b78c17c32db0)

![image](https://github.com/user-attachments/assets/f0a60419-a374-4ea9-b119-75d078dd4460)

![image](https://github.com/user-attachments/assets/9fd5c070-bd76-4f6f-9d72-36d22a0cbe13)

![image](https://github.com/user-attachments/assets/97fbd7b7-a6a1-4528-8474-3f67f9ea6223)




####  כלי שלישי: שימוש באתר [generatedata](https://generatedata.com/generator) על מנת ליצור קובץ SQL, תקיית כל הקבצים: **[`generatedataFiles`](Stage1/generatedataFiles )**  
דוגמא ליצירת הקבצים עבור Sea_vessel:

![image](https://github.com/user-attachments/assets/c25b64a2-7295-4e3e-851b-d13a9bb0adcc)

![image](https://github.com/user-attachments/assets/876d4f0c-4133-4a8d-9054-a4ed0f8aa941)

![image](https://github.com/user-attachments/assets/2f47e4b1-1230-4c7a-9ca3-c92679f7dc11)


### גיבוי

קבצי גיבוי נשמרים עם התאריך של הגיבוי: [לתיקיית הגיבויים](Stage1/Backup)
- ניכנס ל Tools -> Backup וניצור קובץ גיבוי עבור המבנה נתונים שלנו.

![image](https://github.com/user-attachments/assets/d06b82b9-370c-4b5c-8861-a621c13339ad)

![image](https://github.com/user-attachments/assets/9177f5dd-ac51-435b-b024-5cf3732d1287)


- לאחר מכן נבצע Rstore על מנת לראות שהגיבוי עובד:

![image](https://github.com/user-attachments/assets/926e4af5-654e-420c-b4b8-86a150049768)



## שלב 2: שאילתות

###  שאילתות:

####  כל 8 שאילתות הבחירה, 3 המחיקה ו3 העדכון נמצאים בתיקייה:  **[`Queries`](Stage2/Queries)**  
עבור כל שאילתה נראה מה היא עושה, צילום של הרצת השאילתה ותוצאת השאילתה:

- **שאילתות select**

שאילתה מס 1:  ממוצע עומק הצלילה של צוללות לפי דרגת המפקד של הצוות שלהן

![WhatsApp Image 2025-05-04 at 07 09 01_b5cf40cd](https://github.com/user-attachments/assets/5b738bc9-cfb7-43e1-bd3c-6c4e2a392a59)

שאילתה מס 2: סכום התותחים מחולק במספר כלי שיט בכל בסיס

![WhatsApp Image 2025-05-04 at 07 21 22_81f7fd6f](https://github.com/user-attachments/assets/f244f7bc-0816-4c16-9300-8504350ff1b1)

שאילתה מס 3: מוצא את הבסיס עם הכי הרבה כלי ים

![WhatsApp Image 2025-05-04 at 07 23 25_164da695](https://github.com/user-attachments/assets/e4e1592c-7fc5-4383-868c-7df81615cf9f)

שאילתה מס 4: המספר הממוצע של תותחים על ספינות מלחמה בשנה וחודש של תאריך הבדיקה שלהם

![WhatsApp Image 2025-05-04 at 07 26 24_7b60b1fe](https://github.com/user-attachments/assets/dddfd58d-47c0-4c2a-9bfe-05479f96dfd5)

שאילתה מס 5: מחזיר את מספר ספינות מלחמה, צוללות, ספינות טילים ומשחתות לכל בסיס, מקובצים לפי מיקום הבסיס.

![WhatsApp Image 2025-05-04 at 07 31 45_fb05069a](https://github.com/user-attachments/assets/42f91fc4-f150-4950-afce-97ee2657ebb1)

שאילתה מס 6: מחשב את המספר הממוצע של תותחים על ספינות מלחמה לכל בסיס

![WhatsApp Image 2025-05-04 at 07 33 25_50e65200](https://github.com/user-attachments/assets/3ec71d39-f44a-46ca-8c56-9ea8bd787188)

שאילתה מס 7: כל הספינות שבדקו אותן בשנה הנוכחית, כולל שם הצוות, בסיס ומספר חיילים בצוות

![WhatsApp Image 2025-05-04 at 07 34 40_b4ea1665](https://github.com/user-attachments/assets/3fdbdc5e-831f-4d92-b201-588c3e5ae0e2)

שאילתה מס 8: רשימת ספינות שתוקף ההשכרה שלהן יפוג תוך פחות מחצי שנה

![WhatsApp Image 2025-05-04 at 07 36 01_7bb90fc1](https://github.com/user-attachments/assets/e45c885c-7ace-4721-9da9-52437746a4dd)


- **שאילתות delete**

שאילתה מס 1:  מחיקת צוללות שצפיפות החמצן שלהם נמוכה מהממוצע של כמות המשגרים בכלי השיט בתוספת 10

![WhatsApp Image 2025-05-04 at 13 46 59_ef9dbbd5](https://github.com/user-attachments/assets/fdd249d3-8e56-4d3f-a7d5-82581488b918)

שאילתה מס 2: השאילתה מוחקת חיילים בדרגת סיילור שלא משמשים כמפקדים וששייכים לצוותים שלהם כלי שיט שנבדק לפני 2015.



![WhatsApp Image 2025-05-04 at 14 00 48_fa86a4f2](https://github.com/user-attachments/assets/33d2ea1f-8d1e-4393-bec0-875d6192e9a2)


שאילתה מס 3:  מחיקת חיילים שמשרתים בצוותים שלא משויכים לאף כלי שיט, ושדרגתם היא סיילור ושלא משתמשים כמפקדים


![WhatsApp Image 2025-05-04 at 14 03 33_15eaad73](https://github.com/user-attachments/assets/3f729a84-0adc-4d99-8c53-d2cda1e7b2e9)


- **שאילתות update**

שאילתה מס 1:  מעדכן את גודל כל צוות לפי מספר החיילים בו ועוד עשירית מסך הקיבולת של כלי השיט המשויכים לו.

![WhatsApp Image 2025-05-04 at 14 12 25_33804c6e](https://github.com/user-attachments/assets/1547117c-5ea5-48dd-b208-ed02918fe08b)


שאילתה מס 2:  השאילתה מעדכנת את תאריך סיום ההשכרה של כלי שיט שנבדקו לפני 2024 ושייכים לבסיסים שיש בהם לפחות שלושה צוותים שונים, על ידי הוספת חודשיים לתאריך.


![WhatsApp Image 2025-05-04 at 14 17 23_2121865f](https://github.com/user-attachments/assets/77fbd5b3-48d4-43c9-8865-5449b08e6caf)


שאילתה מס 3:  מחיקת צוללות שצפיפות החמצן שלהם נמוכה מהממוצע של כמות המשגרים בכלי השיט בתוספת 10

![WhatsApp Image 2025-05-04 at 14 21 23_1df10989](https://github.com/user-attachments/assets/e4a27b05-b697-4250-9844-1f4b73ad7b84)


###  אילוצים:
אילוץ מס 1: הערך בעמודה max_depth חייב להיות חיובי (גדול מ-0).

![WhatsApp Image 2025-05-04 at 14 28 54_4da9d0f2](https://github.com/user-attachments/assets/1a478504-02b6-4a41-9099-39691a3b2420)


אילוץ מס 2:   עמודת lease_expiration_date הפכה לחובה – אי אפשר להשאיר אותה ריקה.

![WhatsApp Image 2025-05-04 at 14 32 12_0bc2913b](https://github.com/user-attachments/assets/631535ab-3fc7-4f63-a8ba-ad9b5c7e6c60)


אילוץ מס 3:  אם לא מצוין ערך בעמודת rank, תינתן לו ברירת המחדל "sailor".

![WhatsApp Image 2025-05-04 at 14 34 30_589c806a](https://github.com/user-attachments/assets/a8e843f2-25ba-42b6-aa91-835f3b6df82e)


###  RollbackCommit:

- **rollback**

- **שלבים**

- שלב ראשון - begin

![WhatsApp Image 2025-05-04 at 14 47 06_39e721b6](https://github.com/user-attachments/assets/48a53b6a-e02f-4fc9-aa53-0cea0d4abacb)

- שלב שני - עדכון הטבלה

![WhatsApp Image 2025-05-04 at 14 47 21_470d7a6c](https://github.com/user-attachments/assets/b298c88d-8fb6-4741-9661-b9e58593308c)

- שלב שלישי - הדפסת הטבלה המעודכנת

![WhatsApp Image 2025-05-04 at 14 47 38_fae57fc1](https://github.com/user-attachments/assets/a23f85eb-5e97-464c-8c77-ba97293e3b83)

- שלב רביעי - rollback

![WhatsApp Image 2025-05-04 at 14 47 50_417bdf2c](https://github.com/user-attachments/assets/ca340a18-b970-4504-8fda-9f99d2340bde)


- שלב חמישי - הדפסת הטבלה המקורית

![WhatsApp Image 2025-05-04 at 14 48 28_62e523ee](https://github.com/user-attachments/assets/82ff720f-b5d1-4f39-bb00-b223763661d6)


- **commit**


