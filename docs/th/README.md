![GaifaaYeepun](https://user-images.githubusercontent.com/42882840/80269234-b4ad1c80-86e8-11ea-8a02-567b854170d5.png)

![deploy gaifaa](https://github.com/jocv-thai/pleethai/workflows/deploy%20gaifaa/badge.svg)

[日本語](../../README.md) | [English](../en/README.md) | ภาษาไทย

# สรุป
GaifaaYeepun(ไก่ฟ้าญี่ปุ่น) คือเว็บไซต์พจนานุกรมที่สามารถค้นหาคำศัพท์และประโยคในภาษาญี่ปุ่น ภาษาไทยและภาษาอังกฤษได้

เว็บไซต์นี้ ถูกสร้างสำหรับคนไทยที่เรียนภาษาญี่ปุ่น และคนญี่ปุ่นที่เรียนภาษาไทยด้วย

# ความต้องการ
## เซิร์ฟเวอร์

* เว็บเซิร์ฟเวอร์ (Windows Server+IIS)(สำหรับ Production Environment)
* Python(แนะนำ 3.6.7)
* Git

## ไคลเอนต์

* คอมพิวเตอร์ / สมาร์ทโฟน


# การติดตั้ง
- Production Environment (**To Be Determined**)
- [สิ่งแวดล้อมสำหรับการพัฒนา(Development Environment) *ลิงค์ไปยังหน้าภาษาอังกฤษ](../en/install_develop.md)


# วิธีใช้ (สำหรับผู้ใช้ระบบ)
"หน้าค้นหา" คือหน้าหลักที่สามารถกรอกคำศัพท์และประโยคที่ต้องการค้นหาความหมาย

ถ้าผู้ใช้หาคำ(ที่ต้องการค้นหา)ไม่เจอ สามารถใช้ "หน้าขอร้อง" เพื่อส่งอีเมลให้ผู้จัดการเว็ปไซต์ เพื่อเพิ่มเติมและปรับปรุงให้ดียิ่งขึ้นต่อไป

## รายละเอียดของหน้า

- [หน้าค้นหา](./howtouse_search.md)  
[<img src ="https://user-images.githubusercontent.com/42882840/100090635-cf21c100-2e96-11eb-98ec-18694d4d44c9.gif" alt="search demo" width="320">](./howtouse_search.md)

- [หน้าขอร้อง](./howtouse_request.md)  
[<img src ="https://user-images.githubusercontent.com/42882840/100090636-d0eb8480-2e96-11eb-823e-e0059da94e58.gif" alt="request demo" width="320">](./howtouse_request.md)


# การดูแลรักษาระบบ(System Maintenance Procedure)
- วิธีอัพเดทระบบ
  - ได้ไฟล์ใหม่สุดจาก repositoryนี้ แล้วเริ่มเว็บเซิร์ฟเวอร์ใหม่
- [วิธีเพิ่มเติมและปรับปรุงคำศัพท์และประโยค *ลิงค์ไปยังหน้าภาษาอังกฤษ](../en/maintenance_dataedit.md)
- [งานเมื่อได้รับอีเมลขอร้องจากผู้ใช้ *ลิงค์ไปยังหน้าภาษาอังกฤษ](../en/maintenance_reqreceived.md)


# โครงสร้างของระบบ(System Configuration)
- แผนภาพโครงสร้างของระบบ(System Configuration Diagram)  
![System Configuration Diagram](https://docs.google.com/drawings/d/e/2PACX-1vSLFh_yZhKKi0L7hnfksXXx2Rjc6bimx0RjocQRpwrI5KxMZSzmARUx9lNiZXjq-8R6oSboAkMqkxgV/pub?w=2024&h=996)

- [โครงสร้างฐานข้อมูล(Database Structure) *ลิงค์ไปยังหน้าภาษาอังกฤษ](../en/database.md)
