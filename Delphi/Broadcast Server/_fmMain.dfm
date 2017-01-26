object fmMain: TfmMain
  Left = 0
  Top = 0
  Caption = 'Broadcast Server'
  ClientHeight = 412
  ClientWidth = 852
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'Tahoma'
  Font.Style = []
  OldCreateOrder = False
  OnClose = FormClose
  OnCreate = FormCreate
  PixelsPerInch = 96
  TextHeight = 13
  object IdTCPServer: TIdTCPServer
    Bindings = <>
    DefaultPort = 1234
    OnExecute = IdTCPServerExecute
    Left = 64
    Top = 40
  end
end
