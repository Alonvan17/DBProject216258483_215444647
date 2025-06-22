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
  - [שאילתות](#שאילתות)
  - [אילוצים](#אילוצים)  
  - [גיבוי](#גיבוי-2)
- [שלב 3: אינטגרציה ומבטים](#שלב-3-אינטגרציה-ומבטים)
  - [אינטגרציה](#אינטגרציה)
  - [עדכון בסיס נתונים](#עדכון-בסיס-הנתונים)
  - [מבטים](#מבטים)
  - [גיבוי](#גיבוי-3)  
- [שלב 4: תכנות](#שלב-4-תכנות)
  - [פונקציות](#פונקציות)
  - [פרוצדורות](#פרוצדורות)
  - [טריגרים](#טריגרים)
  - [תוכניות](#תוכניות)  







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

###  שאילתות

####  כל 8 שאילתות הבחירה, 3 המחיקה ו3 העדכון נמצאים בתיקייה:  **[`Queries`](Stage2/Queries)**  
עבור כל שאילתה נראה מה היא עושה, צילום של הרצת השאילתה ותוצאת השאילתה:

### Select:

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

לפני:

![image](https://github.com/user-attachments/assets/fc5acc83-b6aa-4dbe-94ff-eb2bd93f5b7e)

אחרי:

![image](https://github.com/user-attachments/assets/11b5af72-51ed-4124-8008-f9ee3ff6f5f9)


שאילתה מס 2: השאילתה מוחקת חיילים בדרגת סיילור שלא משמשים כמפקדים וששייכים לצוותים שלהם כלי שיט שנבדק לפני 2015.


![WhatsApp Image 2025-05-04 at 14 00 48_fa86a4f2](https://github.com/user-attachments/assets/33d2ea1f-8d1e-4393-bec0-875d6192e9a2)

לפני:

![image](https://github.com/user-attachments/assets/ac23b410-ef7f-4d6c-99ec-f004a89e3ebc)

אחרי:

![image](https://github.com/user-attachments/assets/fe936312-2df7-4b07-87ec-0e04b94ae3ca)


שאילתה מס 3:  מחיקת חיילים שמשרתים בצוותים שלא משויכים לאף כלי שיט, ושדרגתם היא סיילור ושלא משתמשים כמפקדים


![WhatsApp Image 2025-05-04 at 14 03 33_15eaad73](https://github.com/user-attachments/assets/3f729a84-0adc-4d99-8c53-d2cda1e7b2e9)

נשאר ללא שינוי אחרי השאילתה.

- **שאילתות update**

שאילתה מס 1:  מעדכן את גודל כל צוות לפי מספר החיילים בו ועוד עשירית מסך הקיבולת של כלי השיט המשויכים לו.

![WhatsApp Image 2025-05-04 at 14 12 25_33804c6e](https://github.com/user-attachments/assets/1547117c-5ea5-48dd-b208-ed02918fe08b)

לפני:


![image](https://github.com/user-attachments/assets/5a53110a-b0d0-4848-b176-6b8bc688ca08)

אחרי:

![image](https://github.com/user-attachments/assets/193599f9-e63b-4c1c-99c6-a353137fc9ba)


שאילתה מס 2:  השאילתה מעדכנת את תאריך סיום ההשכרה של כלי שיט שנבדקו לפני 2024 ושייכים לבסיסים שיש בהם לפחות שלושה צוותים שונים, על ידי הוספת חודשיים לתאריך.

![WhatsApp Image 2025-05-04 at 14 17 23_2121865f](https://github.com/user-attachments/assets/77fbd5b3-48d4-43c9-8865-5449b08e6caf)

לפני: 

![image](https://github.com/user-attachments/assets/35f5b1f6-4363-4ebb-99c0-b6a07cc73d9e)


אחרי:

![image](https://github.com/user-attachments/assets/df0fc20c-1f43-4c40-bfb2-3d7c9f25ae16)



שאילתה מס 3: השאילתה מעדכנת את שמות החיילים בדרגת קפטן בצוותים שלהם יש כלי שיט שנבדקו לפני שנת 2023 ובעלי קיבולת מצטברת גבוהה מ-1, על ידי הוספת תחילית לשם


<img width="959" alt="image" src="https://github.com/user-attachments/assets/06be3975-9240-4ef3-8b51-cae561b3a127" />

לפני:


![image](https://github.com/user-attachments/assets/2c3a1d0c-3c5b-45f3-86f4-49fcfe26994a)

אחרי:

![image](https://github.com/user-attachments/assets/6e6a4fae-746a-440d-9749-4854c4e8ab09)


###  אילוצים:
אילוץ מס 1: הערך בעמודה max_depth חייב להיות חיובי (גדול מ-0).

![WhatsApp Image 2025-05-04 at 14 28 54_4da9d0f2](https://github.com/user-attachments/assets/1a478504-02b6-4a41-9099-39691a3b2420)


אילוץ מס 2:   עמודת lease_expiration_date הפכה לחובה – אי אפשר להשאיר אותה ריקה.

![WhatsApp Image 2025-05-04 at 14 32 12_0bc2913b](https://github.com/user-attachments/assets/631535ab-3fc7-4f63-a8ba-ad9b5c7e6c60)


אילוץ מס 3:  אם לא מצוין ערך בעמודת rank, תינתן לו ברירת המחדל "sailor".

![WhatsApp Image 2025-05-04 at 14 34 30_589c806a](https://github.com/user-attachments/assets/a8e843f2-25ba-42b6-aa91-835f3b6df82e)


###  RollbackCommit:

- **rollback**


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


- שלב ראשון - begin

![image](https://github.com/user-attachments/assets/e42f0423-4d4e-4302-8b53-1ef7437d6f7d)


- שלב שני - עדכון הטבלה

![image](https://github.com/user-attachments/assets/6e6a4318-fa7c-405f-baca-68e5096af2a5)


- שלב שלישי - הדפסת הטבלה המעודכנת

![image](https://github.com/user-attachments/assets/547d9317-6d77-4149-8103-9462bfb27e38)

- שלב רביעי - commit

![image](https://github.com/user-attachments/assets/f1e07131-53eb-4399-803a-c7f1b4a8d37b)


- שלב חמישי - הדפסת הטבלה המעודכנת

![image](https://github.com/user-attachments/assets/8e53dfc8-25db-4b54-b600-476d8d0208a0)


### גיבוי 2

קבצי גיבוי נשמרים עם התאריך של הגיבוי: [לתיקיית הגיבויים](Stage2/Backup)
- ניכנס ל Tools -> Backup וניצור קובץ גיבוי עבור המבנה נתונים שלנו.

![image](https://github.com/user-attachments/assets/d06b82b9-370c-4b5c-8861-a621c13339ad)

![image](https://github.com/user-attachments/assets/d2f73f63-20ef-40bf-8bf2-02d424f01c56)


- לאחר מכן נבצע Rstore על מנת לראות שהגיבוי עובד:

![image](https://github.com/user-attachments/assets/926e4af5-654e-420c-b4b8-86a150049768)

## שלב 3: אינטגרציה ומבטים

הזוג שאנחנו עושים איתו אינטגרציה הם יניב טל ואהוביה בצלאל והנושא שלהם הוא חיל השיריון.

מתוך קובץ הגיבוי שלהם נבנה תרשים DSD:

![DSD Diagram](Stage3/DSD/DSD1.png)  

נבצע reverse engineering:
![ERD Diagram](Stage3/ERD/ERD1.png)  

### אינטגרציה:

לאחר מכן ניצור את הERD  המשותף:

![ERD Diagram](Stage3/ERD/ERD2.png)  

לאחר מחשבה, הבנו שהדרך הנכונה לשלב בין שני תרשימי ה-ERD היא לחבר את סכמת הSoldiers שלנו לסכמת הSoldier של הקבוצה השנייה.
אותו הדבר נעשה לגבי סכמת הCommander.
לאחר מכן, החלטנו שהסכמה crew תהיה הסכמה המקשרת בין התרשימים -  אליה פונות הן הסכמות שלנו, כמו סכמת sea_vessel ו commander והן הסכמות של הקבוצה השנייה, כמו סכמת ה tank.

דיאגרמת DSD משותף:

![DSD Diagram](Stage3/DSD/DSD2.png)  

### עדכון בסיס הנתונים:



✍🏻 **[`Integration.sql`](Stage3/Integration.sql)**  

###  מבטים:
מבט ראשון:

![image](https://github.com/user-attachments/assets/1b71ccaa-e02d-4c24-ba46-b2d17ef6e60d)
![image](https://github.com/user-attachments/assets/0596e042-9c63-4293-be48-1103573c3cb3)


מבט מנקודת המבט של חיל הים 

מה המבט מציג?
המבט v_all_ships מציג רשימה של כל כלי השיט הקיימים במערכת, כולל שיוך שלהם לסוג ספציפי, מיקום הבסיס שלהם, וקיבולת. הוא משלב מידע ממספר טבלאות שקשורות ל־חיל הים, ונותן תצוגה אחודה ונוחה.

שאילתה 1:


![image](https://github.com/user-attachments/assets/01efba25-a182-416c-912a-4f3a27bf362d)

מה היא עושה?

השאילתה תספור ותחזיר את הכמות של כל סוג של ספינות שקיימות במאגר.

![image](https://github.com/user-attachments/assets/3e3908a9-febb-4f5e-9e95-b4725496e5fe)


שאילתה 2:


![image](https://github.com/user-attachments/assets/97b7f9df-7960-4258-a88e-fbcc7fe211ba)

מה היא עושה?
השאילתה תחזיר את כל הבסיסים שמשחתות חונות באותו הבסיס. כאשר מספר המשחתות החונות יחושב ויוצג.

![image](https://github.com/user-attachments/assets/bd6bc67e-2a47-4cb2-8f10-8702386fb8ac)



מבט שני:

![image](https://github.com/user-attachments/assets/754fb8a6-3082-49e6-a08d-ba87474e7c52)
![image](https://github.com/user-attachments/assets/c5ef8837-9612-40d9-a821-f3bcdf5d7d5e)


מבט מנקודת המבט של חיל השריון

מה המבט מציג?
המבט ARMOR_TANKS_MISSIONS_VIEW מציג רשימה של טנקים ופרטי השתתפותם במשימות, והוא מתמקד בנתונים השייכים ל־חיל השריון.


 שאילתה 1:

![image](https://github.com/user-attachments/assets/441c8cca-8d53-4cf7-8cd8-685de4cd1cc4)

מה היא עושה?

מביאה את כל הטנקים והמשימות בהן השתתפו.
מאפשרת לראות מיפוי של כל הטנקים לכל משימה.
![image](https://github.com/user-attachments/assets/10f61f94-01e0-41b3-8905-1c868c63d59e)


שאילתה 2:

![image](https://github.com/user-attachments/assets/61aaa9fd-216e-494a-8051-c45f5c77bb42)

מה היא עושה?

בוחרת רק טנקים שהשתתפו במשימות שהתקיימו לאחר 1 בינואר 2023.
מאפשרת להתמקד במשימות חדשות/עדכניות.

![image](https://github.com/user-attachments/assets/5d6d56d3-9e21-451a-8f3a-338634b77f74)



נראה בבסיס נתונים את שני המבטים שיצרנו:

![image](https://github.com/user-attachments/assets/b7d7ad38-7de8-44bd-8cf4-d81ba8c08ea0)


### גיבוי 3

קבצי גיבוי נשמרים עם התאריך של הגיבוי: [לתיקיית הגיבויים](Stage3/Backup)
- ניכנס ל Tools -> Backup וניצור קובץ גיבוי עבור המבנה נתונים שלנו.

![image](https://github.com/user-attachments/assets/a9406fb0-152c-47de-8c3c-df74972785af)

![image](https://github.com/user-attachments/assets/d2f73f63-20ef-40bf-8bf2-02d424f01c56)


- לאחר מכן נבצע Rstore על מנת לראות שהגיבוי עובד:

![image](https://github.com/user-attachments/assets/926e4af5-654e-420c-b4b8-86a150049768)



## שלב 4: תכנות


### פונקציות:  


פונקציה 1 – ניתוח ביצועי מפקדים 


שם: fn_commander_performance()


✍🏻 **[`function1.sql`](Stage4/Functions/function1.sql)** 

מטרה: לספק מדד איכות על פי מספר טנקים ומבצעים שכל מפקד היה אחראי עליהם.

תיאור כללי:
הפונקציה מחזירה RefCursor עם מידע על מפקדים, כולל דירוג ניסיון ("Experienced", "Intermediate", "Newbie") לפי מספר המשימות שניהלו. הנתונים נאספים מטבלאות Crew, Tank, Unit ו־Mission.

![image](https://github.com/user-attachments/assets/bdb5164c-373d-4b92-a7f6-9c580fce7189)

![WhatsApp Image 2025-06-21 at 22 45 57_c97f2f7b](https://github.com/user-attachments/assets/c79398f7-ea46-4fea-9f03-70343311dac8)


פונקציה 2 – סיכום חיילים לפי יחידות 


שם: fn_soldier_unit_summary(commander_id INT)


✍🏻 **[`function2.sql`](Stage4/Functions/function2.sql)** 

מטרה: להחזיר עבור מפקד מסוים את כל החיילים שתחת פיקודו, כולל היחידה, הטנק והתפקיד שלהם בצוות.

תיאור כללי:
מתבצעים קשרים בין Soldier → Crew → Tank → Unit → CrewMate לפי מזהה מפקד נתון. כל חייל משויך ליחידה ולטנק, ומוצג תפקידו בצוות.

![image](https://github.com/user-attachments/assets/f893cddc-064e-4fa3-a331-779e8b02bad6)

![WhatsApp Image 2025-06-21 at 22 46 37_9f8daca6](https://github.com/user-attachments/assets/3111f6a7-039f-4767-b92d-86689c1774f4)

נסתכל ונראה בבסיס נתונים את העדכון:

![WhatsApp Image 2025-06-21 at 22 46 54_51d5cc19](https://github.com/user-attachments/assets/2278ece6-0902-4ea2-ad49-9d47034264b2)


### פרוצדורות:

### טריגרים:

### תוכניות:







