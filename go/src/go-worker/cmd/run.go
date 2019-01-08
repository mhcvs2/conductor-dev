package cmd

import (
	"github.com/spf13/cobra"
	"go-worker/conductor"
	"go-worker/config"
	"go-worker/task"
)

// runCmd represents the run command
var runCmd = &cobra.Command{
	Use:   "run",
	Short: "A brief description of your command",
	Long: `A longer description that spans multiple lines and likely contains examples
and usage of using your command. For example:

Cobra is a CLI library for Go that empowers applications.
This application is a tool to generate the needed files
to quickly create a Cobra application.`,
	Run: run,
}

func init() {
	rootCmd.AddCommand(runCmd)
}

func run(cmd *cobra.Command, args []string) {
	c := conductor.NewConductorWorker(
		config.ConductorConfig.ServerUrl,
		config.ConductorConfig.ThreadCount,
		10000)

	c.Start("task_1", task.Task_1_Execution_Function, false)
	c.Start("task_5", task.Task_2_Execution_Function, true)
}
