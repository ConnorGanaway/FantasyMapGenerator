using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.IO;
using System.Diagnostics;
using IronPython.Hosting;

namespace FantasyMapGenerator
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            /*
            if (MapView.Visibility == Visibility.Hidden)
            {
                MapView.Visibility = Visibility.Visible;
            }
            else
            {
                MapView.Visibility = Visibility.Hidden;
            }
            */

            var engine = Python.CreateEngine();
            // Path to Python interpreter, Generation Script, and Settings File
            //var python = @"C:\Users\Connor Ganaway\AppData\Local\Microsoft\WindowsApps\python3.exe";
            var pythonScript = @"C:\Users\Connor Ganaway\Desktop\Senior Capstone\FantasyMapGenerator\FantasyMapGenerator\FantasyMapGenerator\noise_gen.py";
            var settingsFile = @"C:\Users\Connor Ganaway\Desktop\Senior Capstone\FantasyMapGenerator\FantasyMapGenerator\FantasyMapGenerator\settings.json";

            var source = engine.CreateScriptSourceFromFile(pythonScript);

            var argv = new List<string>();
            argv.Add("");
            argv.Add(settingsFile);

            engine.GetSysModule().SetVariable("argv", argv);

            var eIO = engine.Runtime.IO;

            var errors = new MemoryStream();
            eIO.SetErrorOutput(errors, Encoding.Default);

            var results = new MemoryStream();
            eIO.SetOutput(results, Encoding.Default);

            var scope = engine.CreateScope();
            source.Execute(scope);

            string str(byte[] x) => Encoding.Default.GetString(x);

            Console.WriteLine("ERRORS");
            Console.WriteLine(str(errors.ToArray()));
            Console.WriteLine();
            Console.WriteLine("RESULTS");
            Console.WriteLine(str(results.ToArray()));
            Console.WriteLine();
        }
    }
}
