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

####  כלי ראשון: יצירת סקריפט בפייתון ✍🏻 **[`insert.py`](Stage1/Programing/insert.py)**  
![image](https://github.com/user-attachments/assets/d2d95a7f-1783-45e1-88da-b78c17c32db0)

![image](https://github.com/user-attachments/assets/f0a60419-a374-4ea9-b119-75d078dd4460)

![image](https://github.com/user-attachments/assets/9fd5c070-bd76-4f6f-9d72-36d22a0cbe13)

![image](https://github.com/user-attachments/assets/97fbd7b7-a6a1-4528-8474-3f67f9ea6223)



####  כלי שני: שימוש באתר [mockaro](https://www.mockaroo.com/) על מנת ליצור קובץ CSV, תקיית כל הקבצים:  **[`mockarooFiles`](Stage1/mockarooFiles)**  
הנה דוגמא ליצירת הקבצים:
עבור Submarine:

![image](https://github.com/user-attachments/assets/19cd2a58-a6a9-43b7-a0a6-00f0dfc4728e)

![image](https://github.com/user-attachments/assets/340ec029-8704-4e78-b625-9b51ae449c85)

ככה נעשה עבור כל הטבלאות


####  כלי שלישי: using [generatedata](https://generatedata.com/generator) to create json file


### גיבוי

קבצי גיבוי נשמרים עם התאריך והשעה של הגיבוי: [לתיקיית הגיבויים](Stage1/Backup)

