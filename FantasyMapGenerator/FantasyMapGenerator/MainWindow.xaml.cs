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
using Newtonsoft.Json;
using System.Threading;
using System.ComponentModel;
using System.Windows.Forms;

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
            //DataContext = new DataStuff("../../../new_map.png");
            this.SizeToContent = SizeToContent.Manual;
            scale.Value = 100;
            octaves.Value = 7;
            persistence.Value = 0.5;
            lacunarity.Value = 1.5;

            SizeInput.Items.Add("500");
            SizeInput.Items.Add("600");
            SizeInput.Items.Add("700");
            SizeInput.Items.Add("800");
            SizeInput.Items.Add("900");
            SizeInput.Items.Add("1000");
            SizeInput.Text = "500";
        }

        private void Seed_Input_TextChanged(object sender, TextChangedEventArgs e)
        {

        }

        private void Generate_Button_Click(object sender, RoutedEventArgs e)
        {
            string tempSize;
            if (string.IsNullOrEmpty(SizeInput.Text))
            {
                tempSize = "500";
            }
            else
            {
                tempSize = SizeInput.Text;
            }
            double tempScale = scale.Value;
            double tempOctaves = octaves.Value;
            double tempPersistence = persistence.Value;
            double tempLacunarity = lacunarity.Value;


            int tempDarkMode = 1;
            if (DarkMode.IsChecked == true)
            {
                tempDarkMode = 0;
            }

            int tempTrees = 0;
            if (Trees.IsChecked == true)
            {
                tempTrees = 1;
            }

            int tempPaths = 0;
            if (Paths.IsChecked == true)
            {
                tempPaths = 1;
            }

            string tempSeed = SeedInput.Text;
            if (tempSeed == "")
            {
                var chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
                var stringChars = new char[16];
                var random = new Random();

                for (int i = 0; i < stringChars.Length; i++)
                {
                    stringChars[i] = chars[random.Next(chars.Length)];
                }

                tempSeed = new String(stringChars);
            }


            string str = "{\n\t\"size\":\"" + tempSize + "\",\n\t\"scale\":\"" + tempScale + "\",\n\t\"octaves\":\"" + tempOctaves + "\",\n\t\"persistence\":\"" + tempPersistence + "\",\n\t\"lacunarity\":\"" + tempLacunarity + "\",\n\t\"day\":\"" + tempDarkMode + "\",\n\t\"trees\":\"" + tempTrees + "\",\n\t\"paths\":\"" + tempPaths + "\",\n\t\"seed\":\"" + tempSeed + "\"\n}";

            File.WriteAllTextAsync("settingsTemp.json", str);


            DateTime time = DateTime.Now;
            tempSeed = tempSeed + time.ToString("h:mm:ss tt");
            string filename = "nm_" + HashString(tempSeed) + ".png";

            string dir = "/maps";

            if (!Directory.Exists(dir)){
                Directory.CreateDirectory(dir);
            }else{
                Directory.Delete(dir, true);
                Directory.CreateDirectory(dir);
            }

            string fullPath = dir + "\\" + filename;

            System.Diagnostics.ProcessStartInfo procStartInfo = new System.Diagnostics.ProcessStartInfo("cmd", "/C python3 ../../../../../noise_gen.py settingsTemp.json");
            procStartInfo.CreateNoWindow = true;
            System.Diagnostics.Process proc = new System.Diagnostics.Process();
            proc.StartInfo = procStartInfo;
            proc.Start();
        }

        private void Trees_Checked(object sender, RoutedEventArgs e)
        {
            
        }

        private void DarkMode_Checked(object sender, RoutedEventArgs e)
        {

        }

        private void Paths_Checked(object sender, RoutedEventArgs e)
        {
            scale.Value = 100;
            octaves.Value = 7;
            persistence.Value = 0.5;
            lacunarity.Value = 1.5;
        }

        private void Buildings_Checked(object sender, RoutedEventArgs e)
        {
            string tempSize;
            if (string.IsNullOrEmpty(SizeInput.Text))
            {
                tempSize = "500";
            }
            else
            {
                tempSize = SizeInput.Text;
            }
            double tempScale = scale.Value;
            double tempOctaves = octaves.Value;
            double tempPersistence = persistence.Value;
            double tempLacunarity = lacunarity.Value;


            int tempDarkMode = 1;
            if (DarkMode.IsChecked == true)
            {
                tempDarkMode = 0;
            }

            int tempTrees = 0;
            if (Trees.IsChecked == true)
            {
                tempTrees = 1;
            }

            int tempPaths = 0;
            if (Paths.IsChecked == true)
            {
                tempPaths = 1;
            }

            string tempSeed = SeedInput.Text;
            if (tempSeed == "")
            {
                var chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
                var stringChars = new char[16];
                var random = new Random();

                for (int i = 0; i < stringChars.Length; i++)
                {
                    stringChars[i] = chars[random.Next(chars.Length)];
                }

                tempSeed = new String(stringChars);
            }

            string str = "{\n\t\"size\":\"" + tempSize + "\",\n\t\"scale\":\"" + tempScale + "\",\n\t\"octaves\":\"" + tempOctaves + "\",\n\t\"persistence\":\"" + tempPersistence + "\",\n\t\"lacunarity\":\"" + tempLacunarity + "\",\n\t\"day\":\"" + tempDarkMode + "\",\n\t\"trees\":\"" + tempTrees + "\",\n\t\"paths\":\"" + tempPaths + "\",\n\t\"seed\":\"" + tempSeed + "\"\n}";

            Stream stream;
            SaveFileDialog saveFileDialog1 = new SaveFileDialog();
            saveFileDialog1.Filter = "JSON File (*.json)|*.json";
            saveFileDialog1.RestoreDirectory = true;
            saveFileDialog1.Title = "Export Settings File";

            DialogResult result = saveFileDialog1.ShowDialog();

            if (result == System.Windows.Forms.DialogResult.OK)
            {
                if ((stream = saveFileDialog1.OpenFile()) != null)
                {
                    // Code to write the stream goes here.
                    byte[] byteArray = Encoding.ASCII.GetBytes(str);
                    MemoryStream mem_stream = new MemoryStream(byteArray);


                    stream.WriteAsync(byteArray, 0, byteArray.Length);  
                    stream.Close();
                }
            }
        }

        private void scale_ValueChanged(object sender, RoutedPropertyChangedEventArgs<double> e)
        {
            if (scale != null)
            {
                scale.Value = Math.Round(scale.Value, 1);
            }
        }

        private void octaves_ValueChanged(object sender, RoutedPropertyChangedEventArgs<double> e)
        {
            if (octaves != null)
            {
                octaves.Value = Math.Round(octaves.Value);
            }
        }

        private void persistence_ValueChanged(object sender, RoutedPropertyChangedEventArgs<double> e)
        {
            if (persistence != null)
            {
                persistence.Value = Math.Round(persistence.Value, 2);
            }
        }

        private void lacunarity_ValueChanged(object sender, RoutedPropertyChangedEventArgs<double> e)
        {
            if (lacunarity != null)
            {
                lacunarity.Value = Math.Round(lacunarity.Value, 2);
            }
        }

        static string HashString(string text, string salt = "")
        {
            if (String.IsNullOrEmpty(text))
            {
                return String.Empty;
            }

            // Uses SHA256 to create the hash
            using (var sha = new System.Security.Cryptography.SHA256Managed())
            {
                // Convert the string to a byte array first, to be processed
                byte[] textBytes = System.Text.Encoding.UTF8.GetBytes(text + salt);
                byte[] hashBytes = sha.ComputeHash(textBytes);

                // Convert back to a string, removing the '-' that BitConverter adds
                string hash = BitConverter
                    .ToString(hashBytes)
                    .Replace("-", String.Empty);

                return hash;
            }
        }

        private void List_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            
        }

        private void Import_Settings_Button_Click(object sender, RoutedEventArgs e)
        {

        }

        private void Create_Report_Button_Click(object sender, RoutedEventArgs e)
        {

        }
    }
}

public class DataStuff
{
    public BitmapImage ImageFilename { 
        get; set; 
    }

    public DataStuff(string imageFilename)
    {
        string[] mapEntries = Directory.GetFiles("/maps");
        System.Diagnostics.Debug.WriteLine(mapEntries[0]);

        ImageFilename = new BitmapImage(new Uri(imageFilename, UriKind.Relative));
    }
}
