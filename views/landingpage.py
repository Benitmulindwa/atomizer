from flet import *

# ---------------------------------------------------------------------------------------------------------------#
## gradient Background ##
# ---------------------------------------------------------------------------------------------------------------#

# Container(
#     # expand=True,
#     height=800,
#     gradient=LinearGradient(
#         begin=alignment.center_left,
#         end=alignment.center_right,
#         colors=["#442063", "#1d3263"],
#     ),
#     alignment=alignment.center,
# ),

# ---------------------------------------------------------------------------------------------------------------#
##LOGO##
# ---------------------------------------------------------------------------------------------------------------#

# Row(
#                 controls=[
#                     Container(height=20, width=20, bgcolor="blue"),
#                     Text("ATOMIZER"),
#                 ],
#                 left=10,
#                 top=5,
#             ),

# ---------------------------------------------------------------------------------------------------------------#
landing_text = Container(
    expand=True,
    width=500,
    content=Text("Your AI-Powered Science Problem - Solving Companion", size=60),
)

landing_text.padding = padding.only(left=20)


def LandingPage(page):
    page.bgcolor = "#1d3263"
    return Column(
        horizontal_alignment=CrossAxisAlignment.CENTER,
        controls=[
            Divider(height=3, color="transparent"),
            Row(
                controls=[
                    Container(height=20, width=20, bgcolor="blue"),
                    Text("ATOMIZER"),
                ],
            ),
            Row(
                # expand=True,
                controls=[
                    landing_text,
                    Container(width=200, height=200, bgcolor="red"),
                ],
            ),
            Container(width=200, expand=True, bgcolor="red"),
        ],
    )
