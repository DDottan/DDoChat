unit _fmMain;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  IdBaseComponent, IdComponent, IdCustomTCPServer, IdTCPServer, IdContext, IdGlobal,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs;

type
  TfmMain = class(TForm)
    IdTCPServer: TIdTCPServer;
    procedure FormCreate(Sender: TObject);
    procedure FormClose(Sender: TObject; var Action: TCloseAction);
    procedure IdTCPServerExecute(AContext: TIdContext);
  private
  public
  end;

var
  fmMain: TfmMain;

implementation

{$R *.dfm}

procedure TfmMain.FormClose(Sender: TObject; var Action: TCloseAction);
begin
  IdTCPServer.Active := false;
end;

procedure TfmMain.FormCreate(Sender: TObject);
begin
  IdTCPServer.Active := true;
end;

procedure TfmMain.IdTCPServerExecute(AContext: TIdContext);
var
  List : TList;
  Loop: Integer;
  Buffer : TIdBytes;
begin
  AContext.Connection.IOHandler.ReadBytes(Buffer, -1);

  List := IdTCPServer.Contexts.LockList;
  try
    for Loop := 0 to List.Count-1 do
        TIdContext(List[Loop]).Connection.IOHandler.Write(Buffer);
  finally
    IdTCPServer.Contexts.UnlockList;
  end;
end;

end.
