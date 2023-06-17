# cms (Compant Management System)
해당 프로그램은 [웹 개발프레임워크] 수업의 기말과제를 위해 만들어졌습니다.<br><BR>
기술 스택 : Python, Django, django-rest-framework, Sqlite <BR>
기능 목록 :
   |페이지 명|기능|
   |---|---|
   |메인|유저별 일정관리 캘린더 (월별,주별,일별)|
   |출근|출퇴근 등록, 출퇴근 조회, 출퇴근 통계|
   |업무보고|업무보고, 승인/반려/결재 기능|
   |자료실|CRUD, 첨부파일 추가|
   |공지사항|CRUD, 첨부파일 추가|
   |Q&A|CRUD, 첨부파일 추가|
   <BR>
   
**🖥 User Interface**
---


메인 페이지
![image](https://github.com/jenjenniee/cms/assets/87688936/8d874db3-0fb5-47bb-9d0d-a8cb3efbbe85)
![image](https://github.com/jenjenniee/cms/assets/87688936/ce9e6f9e-92cb-41a3-849a-c0b85208bd23)
![image](https://github.com/jenjenniee/cms/assets/87688936/e6891a6b-9589-40e3-85a3-8ef8636b3d0e)
<br>
출퇴근 현황
![image](https://github.com/jenjenniee/cms/assets/87688936/e096c079-045b-43a6-8d3c-a54fd6461f1e)
출퇴근 기록
![image](https://github.com/jenjenniee/cms/assets/87688936/a5a7a158-4ab2-4268-8b03-dac48c8d1e1b)
<br>
업무보고 페이지
![image](https://github.com/jenjenniee/cms/assets/87688936/4cbd457b-858a-434a-921c-ec13281ec928)
업무보고 상세 페이지
![image](https://github.com/jenjenniee/cms/assets/87688936/68a53da8-c01d-4583-889d-4b6cbbda413e)
<br>
자료실 목록
![image](https://github.com/jenjenniee/cms/assets/87688936/d559ca2e-d540-44f0-84a5-3cfe0fa7ecda)
자료실 상세페이지
![image](https://github.com/jenjenniee/cms/assets/87688936/406f4d49-b14a-45eb-8953-5df839bdae07)



one to one 매칭, 유저 커스텀(AbstractBaseUser), api, 서버 통신에 대해 공부 
유저 별 다른 달력 db 제공을 위해 one to one 매칭을 사용하여 유저 테이블 확장 
달력 데이터 json 변경 django-rest-framework API 통신
