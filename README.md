Thông tin sinh viên: <br>
Họ và tên: <br>
+ Nguyễn Tấn Khang - MSSV: 23722301 <br>
+ Nguyễn Vũ Hà     - MSSV: 23705991 <br>

### Báo cáo kết quả các bài tập đã làm được của nhóm 
Bài tập <br> 
Báo cáo <br>
Lab 8: <br>
Case 1: Nhóm đã hoàn thành việc tự động cào dữ liệu tỷ giá từ x-rates.com và lưu vào file CSV. Sau đó huấn luyện mô hình RandomForest để phân loại tỷ giá tăng hay giảm và lưu mô hình.<br>
![image](https://github.com/user-attachments/assets/5e191cea-f3d7-424f-8646-435b59bea362) <br>
![image](https://github.com/user-attachments/assets/b365ee69-c93a-4103-b83a-5a0fa1839a90) <br>
Case 2: Nhóm đã hoàn thành việc tự động cào tỷ giá ngoại tệ từ web và lưu vào file rates.csv. Sau đó huấn luyện mô hình phân loại tăng/giảm tỷ giá và in độ chính xác.<br>
![image](https://github.com/user-attachments/assets/d7ce995d-8122-4435-b42e-0e108ca699bc) <br>
![image](https://github.com/user-attachments/assets/ed1198cd-49f5-4a88-9201-2544ea9ba745)<br>


Lab 9: <br>
Exercise-1 Các thành viên đã hoàn chỉnh file *main.py* trong folder của bài tập này. Khi chạy code thì đã tải và giải nén thành công các file trong các URL ban đầu vào folder *downloads* như đề bài yêu cầu, ngoại trừ file *Divvy_Trips_2220_Q1.zip* là bị lỗi không giải nén được. 
Kết quả:<br> 
![image](https://github.com/user-attachments/assets/29df14df-6f52-4791-a6db-1e47b19065ca) <br>



Exercise-2 Các thành viên trong nhóm tìm URL chứa file ghi thông tin khí tượng tại *10:27 ngày 19-01-2024* bằng cách sử dụng *BeautifulSoup* để phân tích cú pháp HTML trả về, tìm được file ghi thông tin khí tượng tại *10:27 ngày 19-01-2024* trong 1 tag \<tr> bên trong \<table>. Sau đó tải về và dùng *Pandas* giải quyết yêu cầu của đề bài. 
![image](https://github.com/user-attachments/assets/70ce7f98-2250-470a-8cec-a3a2f96568b6) <br>

 Exercise-3 Ở bài tập này các thành viên đã dùng các thư viện phù hợp để tải file thứ nhất về tìm URL và tải file thứ 2 về, tuy nhiên file này có chứa nhiều bảng mã của các ngôn ngữ khác nhau nên quá trình giải mã khá phức tạp. Quá trình in ra nội dung của file thứ 2 khá lâu vì file có dung lượng lớn. <br>
 ![image](https://github.com/user-attachments/assets/5494bf03-7573-4384-86f8-8a5e819e71cd) <br>

Exercise-4 Các thành viên đã sử dụng các thư viện phù hợp để tìm các file *.json* trong folder *data*, sau đó chuyển chúng sang file *.csv* bằng các phép biến đổi. 

 ![image](https://github.com/user-attachments/assets/d31a8c04-ad54-4cf1-8d79-89ff7119ba8a)<br>

Exercise-5 Đối với bài tập này, các thành viên đã vận dụng kiến thức, kĩ năng về *Docker* kết hợp với *truy vấn cơ sở dữ liệu* để viết các hàm *kết nối, tạo bảng, ghi dữ liệu* vào cơ sở dữ liệu trên *Postgres* bằng cách sử dụng các *thư viện Python* phù hợp. 
Pipeline Nhóm thống nhất sử dụng Airflow để triển khai pipeline, dùng PostgreSQL để làm cơ sở dữ liệu. Trước tiên, nhóm đã xây dựng file docker-compose để định nghĩa các service có liên quan tới container, nhóm thống nhất định nghĩa service postgres của Exercise-5 vào chúng file docker-compose cho pipeline. Có 1 điểm khác biệt so với khi làm bài tập cá nhân là nhóm đã giới hạn lại số URL để tải file ở Exercise-1 xuống còn 1, ở Exercise-3 nhóm giới hạn chỉ in ra 10000 dòng của file thứ 2 để đỡ tốn thời gian. Sau đó chạy container của pipeline ![](/images/ketqua.png) <br>
![image](https://github.com/user-attachments/assets/d9d2f0d5-24ab-4200-84d2-ab1a70f25fad)<br>

Exercise-6 Thành viên sử dụng thư viện pyspark để hoàn thành phần này, đọc từ 2 file zip mà không cần giải nén, trả lời 6 câu hỏi của bài và được lưu trong thư mục requests
![image](https://github.com/user-attachments/assets/ace93819-c1ab-4f2f-b027-c8039be4782f)<br>

Exercise-7 Mỗi thành viên đã sử dụng thư viện riêng phù hợp của pyspark để hoàn thành bài tập này, file data bên trong đã được các thư viện ấy xử lý. từng thành viên đã hoàn thành được:Thêm tên tệp dưới dạng một cột, Kéo phần datenằm bên trong chuỗi của source_filecột, Thêm một cột mới có tên là brand, Kiểm tra một cột có tên là capacity_bytes, Tạo một cột có tên primary_keylà hashcột tạo nên bản ghi umique trong tập dữ liệu này. <br>
![image](https://github.com/user-attachments/assets/602bfd16-5111-443e-954d-f66b1541d2b1)

