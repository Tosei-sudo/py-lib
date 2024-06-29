using System;
using System.Windows.Forms;

class MsgBox
{
    public static int Main(string[] args)
    {
        if (args.Length == 0)
        {
            return 0;
        }

        string msg = args[0];
        string title = args.Length > 1 ? args[1] : "メッセージ";

        string buttons_str = args.Length > 2 ? args[2] : "OKCancel";
        MessageBoxButtons buttons = MessageBoxButtons.OKCancel;

        switch (buttons_str)
        {
            case "OK":
                buttons = MessageBoxButtons.OK;
                break;
            case "OKCancel":
                break;
            case "YesNo":
                buttons = MessageBoxButtons.YesNo;
                break;
            case "YesNoCancel":
                buttons = MessageBoxButtons.YesNoCancel;
                break;
            case "AbortRetryIgnore":
                buttons = MessageBoxButtons.AbortRetryIgnore;
                break;
            case "RetryCancel":
                buttons = MessageBoxButtons.RetryCancel;
                break;
            default:
                break;
        }

        DialogResult result = MessageBox.Show(msg, title, buttons, MessageBoxIcon.Information);

        return (int)result;
    }
}
