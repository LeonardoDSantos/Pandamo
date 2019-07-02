﻿using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;
using System.Net;
using System.Text;
using System.Threading.Tasks;
using RestSharp;

namespace DynamoPandas
{
    public static class PythonRestCall
    {

        /// <summary>
        /// C# to call Python HttpWeb RESTful API
        /// </summary>
        /// <param name="uirWebAPI">UIR web api link</param>
        /// <param name="exceptionMessage">Returned exception message</param>
        /// <returns>Web response string</returns>
        public static string webUriCaller(string uirWebAPI)
        {
            try
            {
                string webResponse = string.Empty;
                Uri uri = new Uri(uirWebAPI);
                WebRequest httpWebRequest = WebRequest.Create(uri);
                httpWebRequest.ContentType = "application/json";
                WebResponse httpWebResponse = httpWebRequest.GetResponse();
                using (StreamReader streamReader = new StreamReader(httpWebResponse.GetResponseStream()))
                {
                    webResponse = streamReader.ReadToEnd();
                }
                return webResponse;
            }
            catch (WebException ex)
            {
                string exceptionMessage = $"An error occurred:\n";
                if (ex.Status == WebExceptionStatus.ConnectFailure)
                {
                    return exceptionMessage + ex.Message;
                }  
                var resp = new StreamReader(ex.Response.GetResponseStream()).ReadToEnd();
                return exceptionMessage + resp;
            }
        }
    }
}
