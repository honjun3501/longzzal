# 연동테스트
# 파이썬 내장 라이브러리
import tkinter
from tkinter import ttk
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog
import os
import os.path
import shutil
from pathlib import Path
import platform

# 제3자 모듈 라이브러리
from PIL import ImageTk, ImageChops, Image, ImageDraw, ImageFont
import cv2

# 내가 작성한 라이브러리


# 실행파일 만들기
# pyinstaller -w --add-data '/Users/honjun/Desktop/pythonProject/grid_demo_img/*.gif:grid_demo_img' '/Users/honjun/Desktop/pythonProject/main2.py'

# 파일 하나로
# pyinstaller -w --add-data '/Users/honjun/Desktop/pythonProject/grid_demo_img/*.gif:grid_demo_img' '/Users/honjun/Desktop/pythonProject/main2.py' -F

# 파이 인스톨 윈도우
# pyinstaller -w --add-data './grid_demo_img/*.gif:grid_demo_img' './main2.py' -F

# 영상을 새로운 걸로 넣었을때 타깃 영상 정보를 지웠다가 다시 입력하기
# 이전에 입력했던 값을 기억해서 불러오는 기능.
# 자동화 폴더에 넣고 자동시작 버튼 한방에 실행되는 기능
# 영상 캡쳐를 안하고 영상 파일과 자막 파일을 추가할때 비디오 인포 값이 없어서 발생하는 오류
# 같은 파일명이 있으면 다른 파일로 제작
# 사각형 값을 확인 할수 있는 txt 파일 만들기
# 사각형 값을 10단위로 해서 계산해서 그래프로 만들기.
# 배경 스케치북 컬러를 검은색 또는 흰색으로
# 온전한 스크린 샷에서 다시 자막과 영상으로 스샷을 나누는 기능
# 앱 화면면을 4등분, 1, 기본설정과 전체영상 2, 자막과,영상 나누기 3. 실행과정 로그와 마무리.


# ui를 개선하고
# 변수를 좀 정리하고
# 변수명을 정리

# 11 단계의 색깔
# 6단계 버튼색

dark_ocean_color = ['#373B44','#4286f4']

# class LongJjalMaker(Tk):
#     def __init__(self):
#         __init__(self)
#         self.title("LongZZalMaker")
#         self.geometry('1850x780')
#         self.resizable(True, True)
#
#         self.frame_left = None
#         self.frame_right = None
#         self.frame_left_upside = None
#         self.frame_left_downside = None
#         self.frame_right_upside = None
#         self.frame_right_downside = None
#
#         self.frame_browse_path = None
#         self.target_video_path = None
#         self.frame_target_option = None
#         self.lbl_target_a = None
#         self.lbl_target_b = None
#         self.cap_end_time = None
#         self.lbl_end_time = None
#         self.cap_start_time = None
#         self.lbl_start_time = None
#         self.frame_capture_option = None
#         self.lbl_fps = None
#         self.opt_fps = None
#         self.cmb_fps = None
#         self.lbl_crop_ratio = None
#         self.btn_crop_space = None
#         self.lbl_format1 = None
#         self.opt_format1 = None
#         self.cmb_format1 = None
#         self.btn_target_video_path = None
#         self.video_part_frame = None
#         self.video_list_frame = None
#         self.video_scrollbar = None
#         self.video_list_file = None
#
#         self.file_frame1 = None
#         self.btn_add_file1 = None
#         self.btn_del_file1 = None
#         self.lbl_gray_value1 = None
#         self.gray_value1 = None
#         self.contourArea_lbl1 = None
#         self.contourArea_value1 = None
#         self.contours_lbl1 = None
#         self.contours_value1 = None
#         self.btn_del_file12 = None
#         self.sub_lbl_frame = None
#         self.sub_list_frame = None
#         self.sub_scrollbar = None
#         self.sub_list_file = None
#         self.file_frame2 = None
#         self.btn_add_file2 = None
#         self.btn_del_file2 = None
#         self.lbl_gray_value2 = None
#         self.gray_value2 = None
#         self.contourArea_lbl2 = None
#         self.contourArea_value2 = None
#         self.contours_lbl2 = None
#         self.contours_value2 = None
#         self.btn_del_file2 = None
#
#         self.frame_option = None
#         self.lbl_width = None
#         self.opt_width = None
#         self.cmb_width = None
#         self.lbl_space = None
#         self.opt_space = None
#         self.cmb_space = None
#         self.lbl_color = None
#         self.opt_color = None
#         self.cmb_color = None
#         self.lbl_format = None
#         self.opt_format = None
#         self.cmb_format = None
#         self.frame_browse_path = None
#         self.txt_dest_path = None
#         self.btn_dest_path = None
#         self.frame_progress = None
#         self.p_var = None
#         self.progress_bar = None
#         self.frame_run = None
#         self.btn_close = None
#         self.btn_start = None
#         self.btn_tempo = None
#         self.btn_auto_start = None
#
#         self.main()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



class LONG_JJAL_MAKER(Tk):
    def __init__(self):
        super().__init__()
        self.title("LongZZalMaker")
        # self.resizable(False, False)
        self.geometry('1850x780')
        self.resizable(True, True)

# -----------------------------------------------------------------------------------
        # 프레임 골조
        self.frame_left = Frame(self, width=1850/2, height=780, padx=5, pady=5, highlightcolor='green', bg=dark_ocean_color[0])
        self.frame_left.pack(side='left', fill='both', expand=True)
        self.frame_right = Frame(self,width=1850/2, height=780, highlightcolor='green')
        self.frame_right.pack(side='right', fill='both', expand=True)

        self.frame_left_upside = Frame(self.frame_left, relief='solid', bd='1', width=1850/4, height=780/2, padx=5, pady=5, )
        self.frame_left_upside.pack(side='top', fill='both', expand=True)
        self.frame_left_downside = Frame(self.frame_left, relief='solid', bd='1', width=1850/4, height=780/2, padx=5, pady=5, )
        self.frame_left_downside.pack(side='bottom', fill='both', expand=True)

        self.frame_right_upside = Frame(self.frame_right, relief='solid', bd='1', width=1850/4, height=780/2, padx=5, pady=5, )
        self.frame_right_upside.pack(fill='both', expand=True)
        self.frame_right_downside = Frame(self.frame_right, relief='solid', bd='1', width=1850/4, height=780/2, padx=5, pady=5, )
        self.frame_right_downside.pack(fill='both', expand=True)

# ------------------------------------------------------------------------------------
        # 추출할 영상 파일 선택 프레임
        self.frame_browse_path = LabelFrame(self.frame_left_upside, text='추출한 영상 파일 선택')
        self.frame_browse_path.pack(fill='x', padx=5, pady=5, ipady=4)

        self.target_video_path = Entry(self.frame_browse_path)
        self.target_video_path.pack(side='left', fill='x', expand=True, padx=5, pady=5, ipady=4)
        self.btn_target_video_path = Button(self.frame_browse_path, text='찾아보기', width=10,
                                          command=lambda video_save_div_value=1:
                                          self.browse_video_file(video_save_div_value))
        self.btn_target_video_path.pack(side='left', padx=5, pady=5)
# ------------------------------------------------------------------------------------
        # 영상 프레임 정보는 자를 구간 지정 프레임
        self.frame_target_option = LabelFrame(self.frame_left_upside, text='타깃 영상 정보')
        self.frame_target_option.pack(fill='x', padx=5, pady=5, ipady=5)
        # 영상의 총 길이, 프레임
        self.lbl_target_a = ttk.Label(self.frame_target_option, text='전체 재생 시간', width=15, justify='center')
        self.lbl_target_a.pack(side='left', padx=5, pady=5)
        self.lbl_target_b = ttk.Label(self.frame_target_option, text='FPS', width=8, justify='center')
        self.lbl_target_b.pack(side='left', padx=5, pady=5)

        # 종료 시간
        self.cap_end_time = Entry(self.frame_target_option, width=10, justify='center')
        self.cap_end_time.pack(side='right', padx=5, pady=5)
        self.cap_end_time.insert(END, "00:00:00:00")

        # 종료 라벨
        self.lbl_end_time = Label(self.frame_target_option, text='캡쳐 종료 시간', width=13, justify='center')
        self.lbl_end_time.pack(side='right', padx=5, pady=5)

        # 시작 시간
        self.cap_start_time = Entry(self.frame_target_option, width=10, justify='center')
        self.cap_start_time.pack(side='right', padx=5, pady=5)
        self.cap_start_time.insert(END, "00:00:00:00")

        # 시작 라벨
        self.lbl_start_time = Label(self.frame_target_option, text='캡쳐 시작 시간', width=13, justify='center')
        self.lbl_start_time.pack(side='right', padx=5, pady=5)

#------------------------------------------------------------------------------------
        # 캡쳐 옵션 프레임
        self.frame_capture_option = LabelFrame(self.frame_left_upside, text='캡쳐 옵션')
        self.frame_capture_option.pack(fill='x', padx=5, pady=5, ipady=5)

        # 1. FPS 장수 옵션
        self.lbl_fps = Label(self.frame_capture_option, text='1초에 몇장', width=8, justify='center')
        self.lbl_fps.pack(side='left', padx=5, pady=5)
        self.opt_fps = ["3초에 1회", "2초에 1회", "1초에 1회", "1초에 2회"]
        self.cmb_fps = ttk.Combobox(self.frame_capture_option, state='readonly', values=self.opt_fps, width=10, justify='center')
        self.cmb_fps.current(2)
        self.cmb_fps.pack(side='left', padx=5, pady=5)

        # 2. 자막 라인과 화면 분리 지점.£
        self.lbl_crop_ratio = Label(self.frame_capture_option, text='분리 비율', width=8, justify='center')
        self.lbl_crop_ratio.pack(side='left', padx=5, pady=5, ipady=5)
        self.btn_crop_space = Button(self.frame_capture_option, text='분리 지점 설정', width=10,
                                     command=self.crop_ratio_window, justify='center')
        self.btn_crop_space.pack(side='left', padx=5, pady=5)

        # 3. 파일 포맷 옵션
        self.lbl_format1 = Label(self.frame_capture_option, text='형식', width=8, justify='center')
        self.lbl_format1.pack(side='left', padx=5, pady=5)
        self.opt_format1 = ["PNG", "JPG", "BMP"]
        self.cmb_format1 = ttk.Combobox(self.frame_capture_option, state='readonly', values=self.opt_format1, width=10, justify='center')
        self.cmb_format1.current(0)
        self.cmb_format1.pack(side='left', padx=5, pady=5)

        # 3. PNG 캡쳐
        self.btn_target_video_path = Button(self.frame_capture_option, text='PNG 캡쳐 실행', width=10,
                                          command=self.do_img_capture)
        self.btn_target_video_path.pack(side='right', padx=5, pady=5)
# ------------------------------------------------------------------------------------
        # 영상 파일 리스트박스
        self.video_part_frame = LabelFrame(self.frame_left_downside, text='영상 부분')
        self.video_part_frame.pack(fill='both', padx=5, pady=5)
        self.video_list_frame = Frame(self.video_part_frame)
        self.video_list_frame.pack(fill='both')
        self.video_scrollbar = Scrollbar(self.video_list_frame)
        self.video_scrollbar.pack(side='right', fill='y')
        self.video_list_file = Listbox(self.video_list_frame, selectmode='extended', height=20, yscrollcommand=self.video_scrollbar.set)
        self.video_list_file.pack(side='left', fill='both', expand=True)
        self.video_scrollbar.config(command=self.video_list_file.yview)  # 키보드와 마우스 클릭으로도 스크롤바가 작동하게 설정

        # 파일 프레임 (파일 추가, 선택삭제))
        self.file_frame1 = Frame(self.frame_left_downside)
        self.file_frame1.pack(fill='x', padx=5, pady=5)

        self.btn_add_file1 = Button(self.file_frame1, text='영상 부분 파일 추가', padx=5, pady=5, width=10,
                                   command = lambda video_sub_value=1: self.add_file(video_sub_value))
        self.btn_add_file1.pack(side='left')
        self.btn_del_file1 = Button(self.file_frame1, text='선택한 파일 삭제', padx=5, pady=5, width=10,
                                   command=lambda video_sub_value=1: self.del_file(video_sub_value))
        self.btn_del_file1.pack(side='left')

        # 그레이 라벨
        self.lbl_gray_value1 = Label(self.file_frame1, text='GRAY 값', width=10, justify='center')
        self.lbl_gray_value1.pack(side='left', padx=5, pady=5)

        # 그레이 값 입력
        self.gray_value1 = Entry(self.file_frame1, width=3, justify='center')
        self.gray_value1.pack(side='left', padx=5, pady=5)
        self.gray_value1.insert(END, '150')

        # 사각형 라벨
        self.contourArea_lbl1 = Label(self.file_frame1, text='윤곽선 크기', width=8, justify='center')
        self.contourArea_lbl1.pack(side='left', padx=5, pady=5)

        # 사각형 크기 값
        self.contourArea_value1 = Entry(self.file_frame1, width=3, justify='center')
        self.contourArea_value1.pack(side='left', padx=5, pady=5)
        self.contourArea_value1.insert(END, '50')

        # 차이점 개수 라벨
        self.contours_lbl1 = Label(self.file_frame1, text='검출 개수', width=8, justify='center')
        self.contours_lbl1.pack(side='left', padx=5, pady=5)

        # 차이점 개수 값 입력
        self.contours_value1 = Entry(self.file_frame1, width=3, justify='center')
        self.contours_value1.pack(side='left', padx=5, pady=5)
        self.contours_value1.insert(END, '49')

        # 중복 파일 제거
        self.btn_del_file12 = Button(self.file_frame1, text='중복된 이미지 제거', padx=5, pady=5, width=10,
                                    command=lambda doublekiller_var=1:self.doublekiller(doublekiller_var))
        self.btn_del_file12.pack(side='left')
# ------------------------------------------------------------------------------------
        # 자막 리스트 박스
        self.sub_lbl_frame = LabelFrame(self.frame_right_upside, text='자막 부분')
        self.sub_lbl_frame.pack(fill='both', padx=5, pady=5, ipady=5)
        self.sub_list_frame = Frame(self.sub_lbl_frame)
        self.sub_list_frame.pack(fill='both')
        self.sub_scrollbar = Scrollbar(self.sub_list_frame)
        self.sub_scrollbar.pack(side='right', fill='y')
        self.sub_list_file = Listbox(self.sub_list_frame, selectmode='extended', height=20, yscrollcommand=self.sub_scrollbar.set)
        self.sub_list_file.pack(side='left', fill='both', expand=True)
        self.sub_scrollbar.config(command=self.sub_list_file.yview)  # 키보드와 마우스 클릭으로도 스크롤바가 작동하게 설정

        # 파일 프레임
        self.file_frame2 = Frame(self.frame_right_upside)
        self.file_frame2.pack(fill='x', padx=5, pady=5)

        # 파일 추가, 선택삭제 버튼
        self.btn_add_file2 = Button(self.file_frame2, text='자막 부분 파일 추가', padx=5, pady=5, width=12,
                                   command=lambda video_sub_value = 2: self.add_file(video_sub_value))  # command 추가
        self.btn_add_file2.pack(side='left')
        self.btn_del_file2 = Button(self.file_frame2, text='선택한 자막 파일 삭제', padx=5, pady=5, width=12,
                                    command=lambda video_sub_value=2: self.del_file(video_sub_value))
        self.btn_del_file2.pack(side='left')


        # 그레이 라벨
        self.lbl_gray_value2 = Label(self.file_frame2, text='GRAY 값', width=10, justify='center')
        self.lbl_gray_value2.pack(side='left', padx=5, pady=5)

        # 그레이 값 입력
        self.gray_value2 = Entry(self.file_frame2, width=3, justify='center')
        self.gray_value2.pack(side='left', padx=5, pady=5)
        self.gray_value2.insert(END, '150')

        # 사각형 라벨
        self.contourArea_lbl2 = Label(self.file_frame2, text='사각형 값', width=10, justify='center')
        self.contourArea_lbl2.pack(side='left', padx=5, pady=5)

        # 윤곽선 영역 크기값
        self.contourArea_value2 = Entry(self.file_frame2, width=3, justify='center')
        self.contourArea_value2.pack(side='left', padx=5, pady=5)
        self.contourArea_value2.insert(END, '50')

        # 차이점 개수 라벨
        self.contours_lbl2 = Label(self.file_frame2, text='차이점 개수 값', width=10, justify='center')
        self.contours_lbl2.pack(side='left', padx=5, pady=5)

        # 차이점 개수 값 입력
        self.contours_value2 = Entry(self.file_frame2, width=3, justify='center')
        self.contours_value2.pack(side='left', padx=5, pady=5)
        self.contours_value2.insert(END, '100')

        # 중복 파일 제거
        self.btn_del_file2 = Button(self.file_frame2, text='중복된 이미지 제거', padx=5, pady=5, width=12,
                                    command=lambda doublekiller_var=2: self.doublekiller(doublekiller_var))
        self.btn_del_file2.pack(side='left')

# ------------------------------------------------------------------------------------
        # 옵션 프레임1
        self.frame_option = LabelFrame(self.frame_right_downside, text='합치기 옵션')
        self.frame_option.pack(fill='x', padx=5, pady=5, ipady=5)

        # 1. 가로 넓이 옵션
        self.lbl_width = Label(self.frame_option, text='가로넓이', width=8, justify='center')
        self.lbl_width.pack(side='left', padx=5, pady=5)
        self.opt_width = ["원본유지", "1024", "800", "640"]
        self.cmb_width = ttk.Combobox(self.frame_option, state='readonly', values=self.opt_width, width=10, justify='center')
        self.cmb_width.current(0)
        self.cmb_width.pack(side='left', padx=5, pady=5)

        # 2. 간격 옵션
        self.lbl_space = Label(self.frame_option, text='간격', width=8, justify='center')
        self.lbl_space.pack(side='left', padx=5, pady=5)
        self.opt_space = ["없음(0)", "좁게(10)", "보통(20)", "넓게(30)"]
        self.cmb_space = ttk.Combobox(self.frame_option, state='readonly', values=self.opt_space, width=10, justify='center')
        self.cmb_space.current(0)
        self.cmb_space.pack(side='left', padx=5, pady=5)

        # 2. 스케치북 컬러
        self.lbl_color = Label(self.frame_option, text='바탕 색상', width=8, justify='center')
        self.lbl_color.pack(side='left', padx=5, pady=5)
        self.opt_color = ["검은색", "흰색"]
        self.cmb_color = ttk.Combobox(self.frame_option, state='readonly', values=self.opt_color, width=10,
                                      justify='center')
        self.cmb_color.current(0)
        self.cmb_color.pack(side='left', padx=5, pady=5)


        # 3. 파일 포맷 옵션
        self.lbl_format = Label(self.frame_option, text='형식', width=8, justify='center')
        self.lbl_format.pack(side='left', padx=5, pady=5)
        self.opt_format = ["PNG", "JPG", "BMP"]
        self.cmb_format = ttk.Combobox(self.frame_option, state='readonly', values=self.opt_format, width=10, justify='center')
        self.cmb_format.current(0)
        self.cmb_format.pack(side='left', padx=5, pady=5)
# ------------------------------------------------------------------------------------
        # 저장 경로 프레임
        self.frame_browse_path = LabelFrame(self.frame_right_downside, text='저장경로')
        self.frame_browse_path.pack(fill='x', padx=5, pady=5, ipady=5)

        self.txt_dest_path = Entry(self.frame_browse_path)
        self.txt_dest_path.pack(side='left', fill='x', expand=True, padx=5, pady=5, ipady=4)

        self.btn_dest_path = Button(self.frame_browse_path, text='찾아보기', width=10,
                                    command=lambda video_save_div_value=2: self.browse_video_file(video_save_div_value))

        self.btn_dest_path.pack(side='right', padx=5, pady=5)
# ------------------------------------------------------------------------------------
        # 진행 상황 Progress Bar
        self.frame_progress = LabelFrame(self.frame_right_downside, text='진행상황')
        self.frame_progress.pack(fill='x', padx=5, pady=5, ipady=5)
        self.p_var = DoubleVar()
        self.progress_bar = ttk.Progressbar(self.frame_progress, maximum=100, variable=self.p_var)
        self.progress_bar.pack(fill='x', padx=5, pady=5)
# ------------------------------------------------------------------------------------
        # 실행 프레임
        self.frame_run = Frame(self.frame_right_downside)
        self.frame_run.pack(fill='x', padx=5, pady=5)

        self.btn_close = Button(self.frame_run, padx=5, pady=5, text='종료', width=12,
                                command=self.quit)
        self.btn_close.pack(side='right', padx=5, pady=5)
        self.btn_start = Button(self.frame_run, padx=5, pady=5, text='합치기', width=12,
                                command=self.start)
        self.btn_start.pack(side='right', padx=5, pady=5)

        # 자동 실행, 디버깅 버튼
        self.btn_tempo = Button(self.frame_run, padx=5, pady=5, text='중복 제거+텍스트+합치기 ', width=16,
                                command=self.tempo_btn)
        self.btn_tempo.pack(side='left', padx=5, pady=5)
        self.btn_auto_start = Button(self.frame_run, padx=5, pady=5, text='텍스트+합치기', width=12,
                                     command=self.auto)
        self.btn_auto_start.pack(side='left', padx=5, pady=5)
# ------------------------------------------------------------------------------------
# 함수 하나를 만들어서 한번 실행해서 변수를 저장한 딕셔너리를 하나 반환한다. 다음에 사용할 애들은 딕셔너리를 참고한다.
# 아니면 함수의 인자를 넣으면 해당하는 값만 반환한다. if나 더 좋은 구문을 이용해본다.

    def path_manager(self, choice, *args):
        if choice == 'path':
            if args[0] == 'target_video_path':
                result = self.target_video_path.get()
                print(f'{args[0]} : ', result)
                return result

            elif args[0] == 'txt_dest_path':
                result = self.txt_dest_path.get()
                print(f'{args[0]} : ', result)
                return result

        if choice == 'video_capture':
            video = cv2.VideoCapture(self.target_video_path.get())
            if video.isOpened():
                if args[0] == 'video_total_frame':
                    result = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
                    print(f'{args[0]} : ', result)
                    return result
                elif args[0] == 'video_fps':
                    result = video.get(cv2.CAP_PROP_FPS)
                    print(f'{args[0]} : ', result)
                    return result
                elif args[0] == 'video_width':
                    result = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
                    print(f'{args[0]} : ', result)
                    return result
                elif args[0] == 'video_total_frame':
                    result = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
                    print(f'{args[0]} : ', result)
                    return result

                else:
                    return
            video.release()

        if choice == 'file_path':
            if args[0] == 'demo_frame_file':
                file_folder = Path('grid_demo_img/')
                result = str(file_folder / 'demo_frame.png')
                result = resource_path(result)
                print(f'{args[0]} : ', result)
                return result

            elif args[0] == 'demo_grid_file':
                file_folder = Path('grid_demo_img/')
                result = str(file_folder / 'video_subtitle_grid.gif')
                result = resource_path(result)
                print(f'{args[0]} : ', result)
                return result

            elif args[0] == 'mixed_demo_file':
                file_folder = Path('grid_demo_img/')
                result = str(file_folder / 'mixed_demo_frame.png')
                result = resource_path(result)
                print(f'{args[0]} : ', result, type(result))
                return result

            elif args[0] == 'diff_file':
                file_folder = Path('grid_demo_img/')
                result = str(file_folder / 'diff.png')
                result = resource_path(result)
                # print(f'{args[0]} : ', result)
                return result

            elif args[0] == 'save_file_name':
                file_name = "nado_photo." + args[1]
                result = str(Path(self.txt_dest_path.get()) / file_name)
                print(f'{args[0]} : ', result)
                return result

            elif args[0] == 'capture_file':
                filepath = self.target_video_path.get()
                file_name = filepath[:-4] + "/frame%s.{}".format(args[1]) % args[2].zfill(5)
                result = str(Path(file_name))
                # print(f'{args[0]} : ', result)
                return result

            elif args[0] == 'video_file':
                filepath = self.target_video_path.get()
                file_name = filepath[:-4] + '/video_frame/frame%s_a.{}'.format(args[1]) % args[2].zfill(5)
                result = str(Path(file_name))
                # print(f'{args[0]} : ', result)
                return result

            elif args[0] == 'subtitle_file':
                filepath = self.target_video_path.get()
                file_name = filepath[:-4] + '/subtitle_frame/frame%s_b.{}'.format(args[1]) % args[2].zfill(5)
                result = str(Path(file_name))
                # print(f'{args[0]} : ', result)
                return result

    def automation(self):
        # 영상 파일을 불러온다. 혹은 경로를 입력한다.
        # 불러온 경로에서 get_video_info(self): 실행
        pass

    def browse_video_file(self, video_save_div_value):
        # 추출할 영상 파일 선택
        if video_save_div_value == 1:
            video_file_selected = filedialog.askopenfilenames(title="이미지 파일을 선택하세요",
                                                              filetypes=(('MP4 파일', '*.mp4'), ('모든 파일', '*.*')),
                                                              initialdir='./')
            if video_file_selected == '':
                return
            self.target_video_path.delete(0, END)
            self.target_video_path.insert(0, video_file_selected[0])
            self.get_video_info()

        # 저장 경로 선택
        elif video_save_div_value == 2:
            video_folder_selected = filedialog.askdirectory(title="파일을 저장 할 디렉토리를 선택하세요", initialdir='./')

            if video_folder_selected is None or video_folder_selected == '':  # 사용자가 취소를 누를 때. 버그가 발생하는 코드
                return
            self.txt_dest_path.delete(0, END)
            self.txt_dest_path.insert(0, video_folder_selected)

    # 영상의 총 길이와 프레임 정보를 가져와서 라벨에 표시하기
    def get_video_info(self):
        video_total_frame = self.path_manager('video_capture', 'video_total_frame')
        video_fps = self.path_manager('video_capture', 'video_fps')
        playtime = []
        playtime_cal = [60 ** 2 * video_fps, 60 ** 1 * video_fps, video_fps]
        for i in playtime_cal:
            x, y = divmod(video_total_frame, i)
            video_total_frame -= x * i
            playtime += [str(int(x)).zfill(2)]

            # 마지막에 남은 프레임은 그대로 리스트에 담기.
            if i == video_fps:
                playtime += [round(float(y), 2)]
                playtime += [y]

        # print("영상 총 길이 계산 : ", playtime)
        self.lbl_target_a.config(text='{}:{}:{}:{:.2f}'.format(playtime[0], playtime[1], playtime[2], playtime[3]))
        self.lbl_target_b.config(text='{:.2f} FPS'.format(video_fps))

    def crop_ratio_window(self):
        def changeimagesize(max_width, max_height, image):
            width_ratio = max_width / image.size[0]
            height_ratio = max_height / image.size[1]
            new_width = int(width_ratio * image.size[0])
            new_height = int(height_ratio * image.size[1])
            new_image = image.resize((new_width, new_height))
            return new_image

        def crop_slider_report(event):
            self.lbl_crop_ratio["text"] = str(event)

        def create_rect_line(event):
            canvas.delete('line')
            line_y_val = 630 / 100 * crop_slider.get()
            canvas.create_line(0, line_y_val, 1024, line_y_val, fill="red", width=2, tags='line')

        def get_demo_frame():
            filepath = self.path_manager('path', 'target_video_path')
            video = cv2.VideoCapture(filepath)
            video_total_frame = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
            video.set(cv2.CAP_PROP_POS_FRAMES, video_total_frame / 2)
            ret, image = video.read()
            grid_demo_file = self.path_manager('file_path', 'demo_frame_file')
            cv2.imwrite(grid_demo_file, image)
            video.release()

        # 탑 레벨 윈도우 생성
        toplevel = Toplevel(self)
        toplevel.title('영상과 자막 분리 할 비율 정하기')
        toplevel.attributes('-topmost', 'true')
        toplevel.grab_set()

        # 탑레벨 윈도우 프레임, 캔버스
        # img_canvas_frame = Frame(toplevel)
        # img_canvas_frame.pack(fill="both")

        canvas = Canvas(toplevel, width=1024, height=620, bg='gray', bd=10)
        canvas.pack(side='left', expand=True, fill=BOTH)

        # 슬라이더 설정, 위치와 기본값
        crop_slider = Scale(toplevel, from_=1, to=100, command=crop_slider_report, orient=VERTICAL)
        crop_slider.set(75)
        crop_slider.pack(side='right', fill='y', expand=True)

        # 캔버스에 넣을 기본 이미지와 그리드 이미지 합성

        get_demo_frame()

        demo_grid_file = self.path_manager('file_path', 'demo_grid_file')
        demo_frame_file = self.path_manager('file_path', 'demo_frame_file')
        if os.path.isfile(demo_grid_file):
            img_grid_file = Image.open(demo_grid_file)
            img_grid_file_resize = changeimagesize(1024, 600, img_grid_file)
            img_grid_file_convert = img_grid_file_resize.convert("RGBA")
        else:
            msgbox.showwarning('경고', '이미지 그리드 파일이 없습니다.')

        if os.path.isfile(demo_frame_file):
            img_demo_frame = Image.open(demo_frame_file)
            img_demo_frame_resize = changeimagesize(1024, 600, img_demo_frame)
            img_demo_frame_convert = img_demo_frame_resize.convert("RGBA")
        else:
            msgbox.showwarning('경고', '데모 파일이 없습니다.')

        alpha_blended = Image.blend(img_grid_file_convert, img_demo_frame_convert, alpha=.7)
        mixed_demo_file = self.path_manager('file_path', 'mixed_demo_file')
        alpha_blended.save(mixed_demo_file)

        mixed_img = tkinter.PhotoImage(file=mixed_demo_file)
        canvas.create_image(int(mixed_img.width()/2), int(mixed_img.height()/2+10), image=mixed_img)
        crop_slider.bind("<B1-Motion>", create_rect_line)
        toplevel.mainloop()

    def do_img_capture(self):
        def make_directory(filepath):
            directory = Path(filepath[:-4])
            if not os.path.exists(directory):
                os.makedirs(directory)
                os.makedirs(directory / 'video_frame')
                os.makedirs(directory / 'subtitle_frame')
                print("파일 디렉토리 없으면 파일 디렉토리 생성")

            elif os.path.exists(directory):
                shutil.rmtree(directory)
                os.makedirs(directory)
                os.makedirs(directory / 'video_frame')
                os.makedirs(directory / 'subtitle_frame')
                print("파일 디렉토리 있으면 삭제 후 생성")
            else:
                print("파일경로 과련 else 경우")

        def get_crop_ratio():
            if self.lbl_crop_ratio['text'] == '분리 비율':
                result = int(1)
                print("자르는 비율 : ", result)
                return result
            else:
                result = int(self.lbl_crop_ratio['text']) / 100
                print("자르는 비율 : ", result)
                return result

        def get_fps_multiple():
            cmb_fps = self.cmb_fps.get()
            if cmb_fps == "3초에 1회":
                result = 3
                return result
            elif cmb_fps == "2초에 1회":
                result = 2
                return result
            elif cmb_fps == "1초에 1회":
                result = 1
                return result
            elif cmb_fps == "1초에 2회":
                result = 0.5
                return result
            else:
                result = 1
                return result

        def get_img_format():
            result = self.cmb_format1.get().lower()
            return result

        def get_time(video_total_frame, fps):
            start_time = self.cap_start_time.get()
            start_time = list(map(int, start_time.split(":")))
            end_time = self.cap_end_time.get()
            end_time = list(map(int, end_time.split(":")))

            playtime_cal = [60 ** 2 * fps, 60 ** 1 * fps, fps, 1]
            start_frame = 0
            if sum(start_time) == 0:
                start_frame = int(0)
            else:
                for i in range(0, 4):
                    start_frame += start_time[i] * playtime_cal[i]
            if start_frame >= video_total_frame:
                msgbox.showwarning('경고', '시작 시간 설정을 다시 해주세요')

            end_frame = 0
            if sum(end_time) == 0:
                end_frame = video_total_frame
            else:
                for i in range(0, 4):
                    end_frame += end_time[i] * playtime_cal[i]

            if end_frame >= video_total_frame:
                msgbox.showwarning('경고', '종료 시간을 영상의 마지막 프레임으로 설정합니다..')
                end_frame = video_total_frame
            return start_frame, end_frame

        def create_capture_img(filepath, crop_ratio, img_format):
            video = cv2.VideoCapture(filepath)
            if not video.isOpened():
                print("Could not open :", filepath)
                exit(0)

            video_total_frame = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
            img_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
            img_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = video.get(cv2.CAP_PROP_FPS)
            video_cap_fps = fps * fps_multiple
            start_frame, end_frame = get_time(video_total_frame, fps)

            # 캡쳐 시작
            count = 0
            count_str = str(count)
            print("시작 : 끝", start_frame, end_frame)
            print("현재 프레임 번호 : ", video.get(cv2.CAP_PROP_POS_FRAMES))

            duration_frame = end_frame - start_frame
            cap_frame_lst = []

            for i in range(0, int(duration_frame / video_cap_fps) + 1):
                j = start_frame + i * video_cap_fps
                cap_frame_lst += [j]

            for i in cap_frame_lst:
                video.set(cv2.CAP_PROP_POS_FRAMES, int(i))
                ret, image = video.read()

                if crop_ratio == 1:
                    file = self.path_manager("file_path", "capture_file", img_format, count_str)
                    cv2.imwrite(file, image)
                    self.video_list_file.insert(END, file)
                    print('Saved frame number :', int(video.get(0)))
                    count += 1
                    count_str = str(count)

                else:
                    video_img_file = self.path_manager("file_path", "video_file", img_format, count_str)
                    sub_img_file = self.path_manager("file_path", "subtitle_file", img_format, count_str)

                    crop_y_value = int(img_height * crop_ratio)
                    cropped_video_img = image[0:crop_y_value, 0:img_width]  # 세로 범위, 가로범위
                    cropped_sub_img = image[crop_y_value:img_height, 0:img_width]

                    cv2.imwrite(video_img_file, cropped_video_img)
                    cv2.imwrite(sub_img_file, cropped_sub_img)

                    self.video_list_file.insert(END, video_img_file)
                    self.sub_list_file.insert(END, sub_img_file)
                    print('Saved frame number :', int(video.get(0)))
                    count += 1
                    count_str = str(count)

            video.release()
            print("캡쳐 완료")

        filepath = self.path_manager('path', 'target_video_path')

        if filepath is None or filepath is False or filepath == '':
            msgbox.showwarning('경고', '영상 파일 선택을 먼저 해주세요')
            return

        # 캡쳐를 실행하면 리스트박스 삭제
        if len(self.video_list_file.get(0, END)) != 0 or len(self.sub_list_file.get(0, END)) != 0:
            self.video_list_file.delete(0, END)
            self.sub_list_file.delete(0, END)

        make_directory(filepath)
        crop_ratio = get_crop_ratio()
        fps_multiple = get_fps_multiple()
        img_format = get_img_format()
        create_capture_img(filepath, crop_ratio, img_format)

    def add_file(self, video_sub_value):
        files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요", filetypes=(('png 파일', '*.png'), ('모든 파일', '*.*')),
                                            initialdir='./')
        if video_sub_value == 1:
            for file in files:
                self.video_list_file.insert(END, file)

        elif video_sub_value == 2:
            for file in files:
                self.sub_list_file.insert(END, file)

    def del_file(self, video_sub_value):
        if video_sub_value == 1:
            for index in reversed(self.video_list_file.curselection()):
                self.video_list_file.delete(index)
        if video_sub_value == 2:
            for index in reversed(self.sub_list_file.curselection()):
                self.sub_list_file.delete(index)

    def merge_img(self, add_text_onoff):
        def img_add_text(idx, img, sum_image_sorted):
            os_check = platform.platform()
            if os_check[0].lower() == 'windows':
                try:
                    myfont = ImageFont.truetype('Arial Bold.ttf', 60)
                except:
                    myfont = ImageFont.truetype('Arial Bold.otf', 60)
            else:
                try:
                    myfont = ImageFont.truetype('Arial Bold.otf', 60)
                except:
                    myfont = ImageFont.truetype('Arial Bold.ttf', 60)
            target_img = ImageDraw.Draw(img)
            target_img.text((10, 10), "{}".format(Path(sum_image_sorted[idx]).stem), font=myfont, fill=(200, 0, 0))
            return img

        try:
            # 가로 넓이
            img_width = self.cmb_width.get()
            if img_width == "원본유지":
                img_width = -1  # -1일때는 원본 기준으로
            else:
                img_width = int(img_width)

            # 간격
            img_space = self.cmb_space.get()
            if img_space == "좁게(10)":
                img_space = 10
            elif img_space == "보통(20)":
                img_space = 20
            elif img_space == "넓게(30)":
                img_space = 30
            else:  # 없음
                img_space = 0

            # 포맷
            img_format = self.cmb_format.get().lower()
            video_images = list(self.video_list_file.get(0, END))
            sub_images = list(self.sub_list_file.get(0, END))
            sum_image = video_images + sub_images

            sum_image_sorted = sorted(sum_image, key=lambda x: x[-11::])

            for i in sum_image_sorted:
                print(i)

            images = [Image.open(x) for x in sum_image_sorted]

            image_sizes = []
            if img_width > -1:
                image_sizes = [(int(img_width), int(img_width * x.size[1] / x.size[0])) for x in images]

            else:
                image_sizes = [(x.size[0], x.size[1]) for x in images]

            widths, heights = zip(*(image_sizes))
            max_width, total_height = max(widths), sum(heights)

            bg_color = self.cmb_color.get()
            if bg_color == "검은색":
                color = (0, 0, 0)
            elif bg_color == "흰색":
                color = (255, 255, 255)
            else:  # 없음
                color = (0, 0, 0)

            # 스케치북 준비
            if img_space > 0:
                total_height += (img_space * (len(images) - 1))

            result_img = Image.new("RGB", (max_width, total_height), color)
            y_offset = 0

            for idx, img in enumerate(images):
                if add_text_onoff:
                    img_add_text(idx, img, sum_image_sorted)

                if img_width > -1:
                    img = img.resize(image_sizes[idx])

                result_img.paste(img, (0, y_offset))
                y_offset += (img.size[1] + img_space)

                progress = (idx + 1) / len(images) * 100
                self.p_var.set(progress)
                self.progress_bar.update()

            # 포맷 옵션 처리
            file_name_path = self.path_manager('file_path', 'save_file_name', img_format)
            print(file_name_path)
            result_img.save(file_name_path)
            msgbox.showinfo("알림", "작업이 완료되었습니다.")

        except Exception as err:  # 예외처리
            msgbox.showerror("에러", err)

    def start(self):
        # 파일 목록 확인
        if self.video_list_file.size() == 0:
            msgbox.showwarning('경고', '이미지 파일을 추가하세요')
            return

        # 저장 경로 확인
        if len(self.txt_dest_path.get()) == 0:
            msgbox.showwarning('경고', '저장 경로를 선택하세요')
            return

        self.merge_img(add_text_onoff=0)

    def auto(self):
        self.merge_img(add_text_onoff=1)

    def doublekiller(self, doublekiller_var):
        if doublekiller_var == 1:
            double_images = list(self.video_list_file.get(0, END))
            gray_value = int(self.gray_value1.get())
            contours_value = int(self.contours_value1.get())
            contourArea_value = int(self.contourArea_value1.get())

        elif doublekiller_var == 2:
            double_images = list(self.sub_list_file.get(0, END))
            gray_value = int(self.gray_value2.get())
            contours_value = int(self.contours_value2.get())
            contourArea_value = int(self.contourArea_value2.get())

        delete_list = []
        print("자막 영상 파일들 길이 :", len(double_images))

        for i in range(0, len(double_images)):
            if i != (len(double_images)-1):
                previous_img_converted = Image.open(double_images[i]).convert("RGB")
                next_img_converted = Image.open(double_images[i+1]).convert("RGB")
                diff = ImageChops.difference(previous_img_converted, next_img_converted)
                diff_path = self.path_manager('file_path', 'diff_file')
                diff.save(diff_path)

                diff_img = cv2.imread(diff_path)
                gray = cv2.cvtColor(diff_img, cv2.COLOR_BGR2GRAY)
                gray = (gray > gray_value) * gray
                contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                # contours 리스트의 길이 값은 이미지 비교 결과의 검출된 차이점의 개수이다.
                # 일정한 값(예시 250) 갯 수 보다 적게 차이가 나면 같은 사진으로 판단한다는 것이다.
                filtered_contours = []
                # 지정한 윤곽선 크기값 보다 크면 필터링 된 윤곽선 리스트에 포함
                for cnt in contours:
                    if cv2.contourArea(cnt) > contourArea_value:
                        filtered_contours += [cnt]

                print("윤곽선 크기 보다 큰 사각형의 개수 :", len(filtered_contours))

                # 윤곽선 검출 개수가 지정한 값보다 적으면 동일한 이미지로 판단하고 삭제 리스트에 추가해서 삭제.
                if len(filtered_contours) <= contours_value:
                    delete_list += [i]
            else:
                break

        # 첫번째 짤은 남기기
        try:
            del delete_list[0]
        finally:
            pass

        delete_list.reverse()
        if doublekiller_var == 1:
            for index in delete_list:
                self.video_list_file.delete(index)

        elif doublekiller_var == 2:
            for index in delete_list:
                self.sub_list_file.delete(index)

        print("디버깅 완료")

    def tempo_btn(self):
        self.doublekiller(doublekiller_var=1)
        self.doublekiller(doublekiller_var=2)
        self.merge_img(add_text_onoff=1)

if __name__=='__main__':
    app = LONG_JJAL_MAKER()
    app.mainloop()