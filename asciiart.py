SCREEN = """\
|                                                                             ||  / \\\\ \\\\   //^ || //  //^   //                                                   |
| - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ||  \\\\/  //   \\\\  || \\\\ || __  \\\\ - - - - - - - - - - - - - - - - - - - - - - - - - |
| Health: {hp:^8s}  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ||  /\\\\  \\\\    \\\\ || // ||  T  // - - - - - - - - - - - - - - - - - Health: {ehp:^7s} |
| - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ||  \\\\/  //   v// || \\\\  \\\\//  \\\\ - - - - - - - - - - - - - - - - - - - - - - - - - |"""

HEADER = """\
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- ||  / \\\\ \\\\   //^ || //  //^   //   - - Map Danger: {0:<23} - Health: {1:<5} - - - - - - - - - - - - - - - - - - - - - - - - - - - - - Floor: {4:<3}-
- ||  \\\\/  //   \\\\  || \\\\ || __  \\\\   - - Hide Danger: {6:<23}- Potions: {2:<4} - Repellant: {10:<4} - Active For: {11:<4}  - - - - - - - - - - - - - - - -
- ||  /\\\\  \\\\    \\\\ || // ||  T  //   - - Escape Chance: {7:<16} - - - Candles: {8:<4} - Fireballs: {9:<4} - - - - - - - - - - - - - - - - - - - - - - - - - -
- ||  \\\\/  //   v// || \\\\  \\\\//  \\\\   - - Moves Remaining: {5:<4} - Game Message: {3:<81} -"""
    
HELP_HEADER = """\
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- ||  / \\\\ \\\\   //^ || //  //^   //   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
- ||  \\\\/  //   \\\\  || \\\\ || __  \\\\   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
- ||  /\\\\  \\\\    \\\\ || // ||  T  //   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
- ||  \\\\/  //   v// || \\\\  \\\\//  \\\\   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"""

SHIELD = """
|`-._/\_.-`|
|___o()o___|
|__((<>))__|
\   o\/o   /
  '. || .'
     ''
"""

CLAWS = """
  ______    
 / - -  )   
 v^v^v^v    
  ______    
 / - -  )   
 v^v^v^v    
"""

SWORD = """
__)(__
'-<>-'
  )(
  ||
  ||
  \/
"""

BOW = """
( 
 \   ^ ^ ^ 
 |)  | | | 
 |)  | | | 
 /   | | | 
(    # # #
"""

CLUB = """
      __
     /||\ 
     \||/
      ][
      ][
      ]["""


CHARACTER3 = """\
|      _,.
|    ,` -.)
|   ( _/-\\\\-._
|  /,|`--._,-^|          ,
|  \_| |`-._/||        ,'|
|    |  `-, / |       /  /
|    |     || |      /  /
|     `r-._||/   __ /  /
|'  \   `---'   \  /  / 
|    /           //  /
|\_/' \         |/  /
| |    |   _,^-'/  / 
| |    , ``  (\/  /_
|  \,.->._    \X-=/^
|  (  /   `-._//^` """

GOBLIN = """\
  /\\              ,      ,           |
  ||              /(.-""-.)\\         |
  ||         | \ / =.  .= \ / |      |
  ||         \( \   o\/o   / )/      |
  ||          \_, '-/  \-' ,_/       |
  ||            /   \__/             |
  ||          ___\ \|--|/ /___       |
  ||         /`    \      /    `\\    |
  ||        |      \_ _ /     |      |
  ||________/                 |      |
  88________       X X X      |      |
  ||          \              /       |
  ||           \           /         |
  ||            | = = = = |          |
  ||            | |     | |          |"""


DEAD_GOBLIN = """\
  /\\              ,      ,           |
  ||              /(.-""-.)\\         |
  ||         | \ / =.  .= \ / |      |
  ||         \( \   x\/x   / )/      |
  ||          \_, '-/  \-' ,_/       |
  ||            /   \__/             |
  ||          ___\ \|--|/ /___       |
  ||         /`    \      /    `\\    |
  ||        |      \_ _ /     |      |
  ||________/                 |      |
  88________       X X X      |      |
  ||          \              /       |
  ||           \           /         |
  ||            | = = = = |          |
  ||            | |     | |          |"""

SKELETON = """\
                 .-"```"-.                      |
                /         \\                     |
                | (_\\ /_) |                     |
                (_   A   _)                     |
                 | _____ |                      |
     ^           \\`\"\"\"\"`/                       |
   /   \\           _:=:_                   \\|   |
   \\   /    .-~~~` _:=:_`~~~-.           \\///   |
    | |    (`,-- -`\\   /`- --,`)         (`/    |
    | |   / /(_-_  _| |_  _-_)\\ \\       ///     |
    | |  / / (_- __ \\ / __ -_) \\ \\     ///      |
    | | / /  (_ -_ - ^ - _- _)  \\ \\   ///       |
    | |/ /   (_-  _ /=\\ _ - _)   \\ \\ '//        |
    | / /     (_ -.':=:'. -_)     \\ \\//         |"""

DEAD_SKELETON = """\
                 .-"```"-.                      |
                /         \\                     |
                | (X) (X) |                     |
                (_   A   _)                     |
                 | _____ |                      |
     ^           \\`\"\"\"\"`/                       |
   /   \\           _:=:_                   \\|   |
   \\   /    .-~~~` _:=:_`~~~-.           \\///   |
    | |    (`,-- -`\\   /`- --,`)         (`/    |
    | |   / /(_-_  _| |_  _-_)\\ \\       ///     |
    | |  / / (_- __ \\ / __ -_) \\ \\     ///      |
    | | / /  (_ -_ - ^ - _- _)  \\ \\   ///       |
    | |/ /   (_-  _ /=\\ _ - _)   \\ \\ '//        |
    | / /     (_ -.':=:'. -_)     \\ \\//         |"""

TROLL = """\
             ,='`````'=                         |
            / (o)/ (o)  \\            _,-,       |
            |    (_,    |        ,-'`_,-\\       |
        ,-~~~\\  `===`'  /-,      \\==```` \\__    |
       /        `----'     `\\     \\       \\/    |
   /      ,               \\,-`\\`_,-`\\_,..--'\\   |
  ,`    ,/,              ,>,   )     \\--`````\\  |
  (      `\\`---'`  `-,-'`_,<   \\      \\_,.--'`  |
   `.      `--. _,-'`_,-`  |    \\               |
    [`-.___   <`_,-'`------(    /               |
    (`` _,-\\   \\ --`````````|--`                |
     >-`_,-`\\,-` ,          |                   |
   <`_,'     ,  /\\          /                   |
    `  \\/\\,-/ `/  \\/`\\_/V\\_/                    |
       (  ._. )    ( .__. )                     |"""

DEAD_TROLL = """\
             ,='`````'=                         |
            / (x)/ (x)  \\            _,-,       |
            |    (_,    |        ,-'`_,-\\       |
        ,-~~~\\  `===`'  /-,      \\==```` \\__    |
       /        `----'     `\\     \\       \\/    |
   /      ,               \\,-`\\`_,-`\\_,..--'\\   |
  ,`    ,/,              ,>,   )     \\--`````\\  |
  (      `\\`---'`  `-,-'`_,<   \\      \\_,.--'`  |
   `.      `--. _,-'`_,-`  |    \\               |
    [`-.___   <`_,-'`------(    /               |
    (`` _,-\\   \\ --`````````|--`                |
     >-`_,-`\\,-` ,          |                   |
   <`_,'     ,  /\\          /                   |
    `  \\/\\,-/ `/  \\/`\\_/V\\_/                    |
       (  ._. )    ( .__. )                     |"""

BLANK_ENEMY = """\
                         |
                         |
                         |
                         |
                         |
                         |
                         |
                         |"""

STEVENDORF = """\
                   _.--.    .--._
                 ."  ."      ".  ".
                ;  ."    /\\    ".  ;
                ;  '._,-/  \\-,_.`  ;
                \\  ,`  / /\\ \\  `,  /
                 \\/    \\/  \\/    \\/
                 |  "_   \\/   _"  |
                 |_   '"-..-"'   _|
                 | "-.        .-" |
                 |    "\\    /"    |
     _,-",  ",   '_     |  |     _'   ,"  ,"-,_
   _(  \\  \\   \\"=--"-.  |  |  .-"--="/   /  /  )_
 ,"  \\  \\  \\   \\      "-'--'-"      /   /  /  /  "."""

DEAD_STEVENDORF = """\
                   _.--.    .--._
                 ."  ."      ".  ".
                ;  ."    /\\    ".  ;
                ;  '._,-/  \\-,_.`  ;
                \\  ,`  / /\\ \\  `,  /
                 \\/    \\/  \\/    \\/
                 |  "_   \\/   _"  |
                 |_   '"-..-"'   _|
                 | "-.        .-" |
                 |    "\\    /"    |
     _,-",  ",   '_     |  |     _'   ,"  ,"-,_
   _(  \\  \\   \\"=--"-.  |  |  .-"--="/   /  /  )_
 ,"  \\  \\  \\   \\      "-'--'-"      /   /  /  /  "."""

RAT = """              |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
     (_(               |
    ('')               |
  _  "\ )>,_     .-->  |
  _>--w/((_ >,_.'      |
         ///           |
         "`"           |"""

DEAD_RAT = """              |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
     (_(               |
    (XX)               |
  _  "\ )>,_     .-->  |
  _>--w/((_ >,_.'      |
         ///           |
         "`"           |"""

DOG = """                        |
                /\_/\____,       |
      ,___/\_/\ \  ~     /       |
      \     ~  \ )   XXX         |
        XXX     /    /\_/\___,   |
           \o-o/-o-o/   ~    /   |
            ) /     \    XXX     |
           _|    / \ \_/         |
        ,-/   _  \_/   \         |
       / (   /____,__|  )        |
      (  |_ (    )  \) _|        |
     _/ _)   \   \__/   (_       |
    (,-(,(,(,/      \,),),)      |"""

DEAD_DOG = """                   |
                /\_/\____,       |
      ,___/\_/\ \  x     /       |
      \     x  \ )   xxx         |
        xxx     /    /\_/\___,   |
           \o-o/-o-o/   x    /   |
            ) /     \    xxx     |
           _|    / \ \_/         |
        ,-/   _  \_/   \         |
       / (   /____,__|  )        |
      (  |_ (    )  \) _|        |
     _/ _)   \   \__/   (_       |
    (,-(,(,(,/      \,),),)      |"""


DRAGON = """                               |
    <>=======()                            |
   (/\___   /|\\          ()==========<>_  |
         \_/ | \\        //|\   ______/ \) |
           \_|  \\      // | \_/           |
             \|\/|\_   //  /\/             |
              (oo)\ \_//  /                |
             //_/\_\/ /  |                 |
            @@/  |=\  \  |                 |
                 \_=\_ \ |                 |
                   \==\ \|\_               |
                __(\===\(  )\              |
                    ______/ /              |
                    '------'               |"""


DEAD_DRAGON = """                          |
    <>=======()                            |
   (/\___   /|\\          ()==========<>_  |
         \_/ | \\        //|\   ______/ \) |
           \_|  \\      // | \_/           |
             \|\/|\_   //  /\/             |
              (xx)\ \_//  /                |
             //_/\_\/ /  |                 |
            @@/  |=\  \  |                 |
                 \_=\_ \ |                 |
                   \==\ \|\_               |
                __(\===\(  )\              |
                    ______/ /              |
                    '------'               |"""
