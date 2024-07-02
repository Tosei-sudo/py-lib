using System;
using System.Windows.Forms;

static class FolderDialog
{
    [STAThread]
    public static void Main()
    {
        FolderBrowserDialog fbDialog = new FolderBrowserDialog();

        // ダイアログの説明文を指定する
        fbDialog.Description = "ダイアログの説明文";

        // デフォルトのフォルダを指定する
        fbDialog.SelectedPath = @"C:";

        // 「新しいフォルダーの作成する」ボタンを表示する
        fbDialog.ShowNewFolderButton = true;

        //フォルダを選択するダイアログを表示する
        if (fbDialog.ShowDialog() == DialogResult.OK)
        {
            Console.WriteLine(fbDialog.SelectedPath);
        }

        // オブジェクトを破棄する
        fbDialog.Dispose();
    }
}