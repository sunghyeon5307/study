using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using OpenCvSharp;

namespace opencvsharp_cam
{
    public partial class Form1 : Form
    {
        private VideoCapture vc;
        private VideoWriter vw = new VideoWriter();
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            timer1.Enabled = false;
            try
            {
                vc.Dispose();
            }
            catch { }
            vc = new VideoCapture(0);
            timer1.Enabled = true;                 
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            Mat frame = new Mat();
            vc.Read(frame);
            if (frame.Empty()) return;
            else
            {
                try
                {
                    this.Invoke((Action)(() =>
                    {
                        vw.Write(frame);
                        pictureBox1.Image = OpenCvSharp.Extensions.BitmapConverter.ToBitmap(frame);
                    }), null);
                }
                catch { }
            }
        }
    }
}
