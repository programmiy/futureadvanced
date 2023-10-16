# 컴파일할 C 파일 이름
$filename = "example"

# 입력값으로 받은 C 파일 이름으로 변경
if ($args.Length -gt 0) {
  $filename = $args[0]
}

# Visual Studio의 경로
$vs_path = "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build"

# 시스템 PATH에 Visual Studio의 경로 추가
$env:Path += ";$vs_path"

# C 파일을 컴파일하여 실행 파일 생성
cl.exe /Fe:$filename.exe $filename.c

# 실행 파일 실행
./$filename.exe