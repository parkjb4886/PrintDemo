# 1 pip install rich가 필요합니다.
from rich import print as rprint
from rich.table import Table
from rich.panel import Panel

# 6 변수
name = "Alice"
age = 25
score = 90.5

data = {'name': name, 'age': age, 'score': score}

# 12 # 1) 컬러/스타일링 출력 (f-string)
rprint(f'[bold green]Hello[/bold green], {name}! Your score is [cyan]{score:.2f}[/cyan]!')

# 15 # 2) 패널(박스)로 딕셔너리 출력
panel_text = (
    f'[bold]Student Info[/]\n'
    f'Name: [yellow]{name}[/]\n'
    f'Age: [magenta]{age}[/]\n'
    f'Score: [cyan]{score:.2f}[/]'
)

rprint(Panel(panel_text, title="Profile", border_style="blue"))

# 24 # 3) 테이블 출력 (딕셔너리 리스트 보기 좋게)
table = Table(title="Records")
table.add_column("Key", style="bold")
table.add_column("Value")

for k, v in data.items():
    table.add_row(k, str(v))
    
rprint(table)

# 33 # 4) sep, end 옵션 그대로 활용 (rich.print도 동일 동작)
rprint("2025", "09", "30", sep=" - ", end="!\n")