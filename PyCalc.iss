[Setup]
AppName=PyCalc
AppVerName=PyCalc v1.5
AppPublisher=Chill-Astro
DefaultDirName={autopf}\Chill-Astro\PyCalc
DefaultGroupName=Chill-Astro                 
UninstallDisplayIcon={app}\Pycalc.exe
DisableWelcomePage=no
Compression=lzma2               
SolidCompression=yes            
ArchitecturesAllowed=x64compatible 
ArchitecturesInstallIn64BitMode=x64compatible 
OutputDir=Output                
OutputBaseFilename=PyCalc-Setup 
WizardStyle=modern            

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\Master\Chill-Astro\PyCalc\dist\*"; DestDir: "{app}"; Flags: recursesubdirs createallsubdirs

[Icons]
Name: "{group}\PyCalc"; Filename: "{app}\PyCalc.exe"; IconFilename: "{app}\PyCalc.ico"
Name: "{commondesktop}\PyCalc"; Filename: "{app}\PyCalc.exe"; IconFilename: "{app}\PyCalc.ico"; Tasks: desktopicon

[Registry]
Root: HKLM; Subkey: "SYSTEM\CurrentControlSet\Control\Session Manager\Environment"; ValueName: "Path"; ValueType: expandsz; ValueData: "{olddata};{app}"; 