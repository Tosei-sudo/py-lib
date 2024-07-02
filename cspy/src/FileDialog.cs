using System;
using System.Windows.Forms;

class FileDialog
{
    [STAThread]
    public static void Main(string[] args)
    {
        // 必要なアプリケーション初期化
        Application.EnableVisualStyles();
        Application.SetCompatibleTextRenderingDefault(false);

        string Filter = args.Length > 0 ? args[0] : "All files (*.*)|*.*";
        bool Multiselect = args.Length > 1 ? args[1] == "true" : false;

        // ファイルダイアログのインスタンスを作成
        OpenFileDialog openFileDialog = new OpenFileDialog
        {
            Filter = Filter,
            FilterIndex = 1,
            RestoreDirectory = true,
            Multiselect = Multiselect
        };

        // ダイアログを表示する
        DialogResult result = openFileDialog.ShowDialog();

        if (result == DialogResult.OK)
        {
            if (Multiselect)
            {
                foreach (string filename in openFileDialog.FileNames)
                {
                    Console.WriteLine(filename);
                }
            }
            else
            {
                Console.WriteLine(openFileDialog.FileName);
            }
        }
    }
}
