[Setup]
AppName=PyCalc
AppVersion=1.0
DefaultDirName={pf}\YourAppName
DefaultGroupName=YourAppName
OutputBaseFilename=YourAppNameInstaller
Compression=lzma
SolidCompression=yes

[Files]
Source: "C:\Users\Master\Desktop\PyCalc.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\YourAppName"; Filename: "{app}\yourapp.exe"
Name: "{group}\PyC"; Filename: "{app}\yourapp.exe"
Name: "{group}\Pycalc"; Filename: "{app}\yourapp.exe"
Name: "{commondesktop}\PyC"; Filename: "{app}\yourapp.exe"
Name: "{commondesktop}\Pycalc"; Filename: "{app}\yourapp.exe"

[Run]
Filename: "{app}\PyCalc.exe"; Description: "Launch PyCalc"; Flags: nowait postinstall skipifsilent
