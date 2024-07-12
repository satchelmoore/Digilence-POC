using System;
using System.IO;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        // Create a new instance of HttpClient
        using (HttpClient client = new HttpClient())
        {
            // Set the base address of the API
            client.BaseAddress = new Uri("http://127.0.0.1:8000");

            // Create a new MultipartFormDataContent object
            using (var form = new MultipartFormDataContent())
            {
                // Add form data
                form.Add(new StringContent("question"), "what is the summary of the document?");

                // Add the file name
                var filePath = "test2.doc";
                using (var fileStream = new FileStream(filePath, FileMode.Open, FileAccess.Read))
                {
                    var fileContent = new StreamContent(fileStream);
                    fileContent.Headers.ContentType = MediaTypeHeaderValue.Parse("multipart/form-data");
                    form.Add(fileContent, "file", Path.GetFileName(filePath));
                    
                    // Send a POST request to the API
                    HttpResponseMessage response = await client.PostAsync("upload", form);

                    // Ensure the request was successful
                    response.EnsureSuccessStatusCode();

                    // Read the response content as a string
                    string responseBody = await response.Content.ReadAsStringAsync();

                    // Print the response body
                    Console.WriteLine(responseBody);
                }
            }
        }
    }
}
