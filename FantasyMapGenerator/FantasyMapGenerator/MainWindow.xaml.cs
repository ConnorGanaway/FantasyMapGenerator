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
            
            if (MapView.Visibility == Visibility.Hidden)
            {
                MapView.Visibility = Visibility.Visible;
            }
            else
            {
                MapView.Visibility = Visibility.Hidden;
            }

            string tempSize = SizeInput.Text;
            if (tempSize == "")
            {
                tempSize = "500";
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


            string str = "{\n\t\"size\":\"" + tempSize + "\",\n\t\"scale\":\"" + tempScale + "\",\n\t\"octaves\":\"" + tempOctaves + "\",\n\t\"persistence\":\"" + tempPersistence + "\",\n\t\"lacunarity\":\"" + tempLacunarity + "\",\n\t\"day\":\"" + tempDarkMode + "\",\n\t\"seed\":\"" + tempSeed + "\"\n}";

            File.WriteAllTextAsync("settingsTemp.json", str);


            System.Diagnostics.ProcessStartInfo procStartInfo = new System.Diagnostics.ProcessStartInfo("cmd", "/k python3 ../../../../../noise_gen.py settingsTemp.json");
            procStartInfo.CreateNoWindow = false;
            System.Diagnostics.Process proc = new System.Diagnostics.Process();
            proc.StartInfo = procStartInfo;
            proc.Start();
        }

        //TBD Generation Option (This is being used as a reset button for the values at the moment
        private void CheckBox_Checked_3(object sender, RoutedEventArgs e)
        {
            scale.Value = 100;
            octaves.Value = 7;  
            persistence.Value = 0.5;
            lacunarity.Value = 1.5;
        }

        private void TextBox_TextChanged_1(object sender, TextChangedEventArgs e)
        {

        }

        private void TextBox_TextChanged(object sender, TextChangedEventArgs e)
        {

        }

        private void DarkMode_Checked(object sender, RoutedEventArgs e)
        {

        }

        private void Paths_Checked(object sender, RoutedEventArgs e)
        {

        }

        private void CheckBox_Checked_4(object sender, RoutedEventArgs e)
        {

        }

        private void scale_ValueChanged(object sender, RoutedPropertyChangedEventArgs<double> e)
        {

        }

        private void octaves_ValueChanged(object sender, RoutedPropertyChangedEventArgs<double> e)
        {

        }

        private void persistence_ValueChanged(object sender, RoutedPropertyChangedEventArgs<double> e)
        {

        }

        private void lacunarity_ValueChanged(object sender, RoutedPropertyChangedEventArgs<double> e)
        {

        }
    }
}
